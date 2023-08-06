from __future__ import annotations

import re
from typing import Any

from ikea_api.api import API, Method
from ikea_api.constants import Constants, Secrets
from ikea_api.endpoints.cart import Cart
from ikea_api.errors import IkeaApiError, OrderCaptureError


class OrderCapture(API):
    def __init__(self, token: str, zip_code: str | int, state_code: str | None = None):
        super().__init__(token, "https://ordercapture.ikea.ru/ordercaptureapi/ru")

        if Constants.COUNTRY_CODE != "ru":
            self._endpoint = (
                "https://ordercapture.ingka.com/ordercaptureapi/"
                + Constants.COUNTRY_CODE
            )

        zip_code = str(zip_code)
        validate_zip_code(zip_code)
        self._zip_code = zip_code

        validate_state_code(state_code)
        self._state_code = state_code

        self._session.headers["X-Client-Id"] = Secrets.purchases_x_client_id

    def __call__(self) -> list[dict[str, Any]]:
        return self.get_delivery_services()

    def _error_handler(self, status_code: int, response: dict[Any, Any]):
        if "errorCode" in response:
            raise OrderCaptureError(response)

    def _get_items_for_checkout_request(self):
        cart = Cart(self._token)
        cart_show = cart.show()
        items_templated: list[dict[str, Any]] = []
        try:
            if cart_show.get("data"):
                for d in cart_show["data"]["cart"]["items"]:
                    items_templated.append(
                        {
                            "quantity": d["quantity"],
                            "itemNo": d["itemNo"],
                            "uom": d["product"]["unitCode"],
                        }
                    )
        except KeyError:
            pass
        return items_templated

    def _get_checkout(self):
        """Generate checkout for items"""
        items = self._get_items_for_checkout_request()
        if len(items) == 0:
            return

        data = {
            "shoppingType": "ONLINE",
            "channel": "WEBAPP",
            "checkoutType": "STANDARD",
            "languageCode": Constants.LANGUAGE_CODE,
            "items": items,
            "deliveryArea": None,
        }

        response: dict[str, str] = self._call_api(
            endpoint=f"{self._endpoint}/checkouts",
            headers={"X-Client-Id": Secrets.purchases_checkout_x_client_id},
            data=data,
        )

        if "resourceId" in response:
            return response["resourceId"]
        raise IkeaApiError("No resourceId for checkout")

    def _get_delivery_area(self, checkout: str | None):
        """Generate delivery area for checkout from Zip Code and State Code"""
        data = {"enableRangeOfDays": False, "zipCode": self._zip_code}
        if self._state_code is not None:
            data["stateCode"] = self._state_code
        response = self._call_api(
            f"{self._endpoint}/checkouts/{checkout}/delivery-areas", data=data
        )

        if "resourceId" in response:
            return response["resourceId"]
        else:
            raise IkeaApiError("No resourceId for delivery area")

    def get_delivery_services(self):
        """Get available delivery services"""
        checkout: str | None = self._get_checkout()
        delivery_area = self._get_delivery_area(checkout)

        response = self._call_api(
            f"{self._endpoint}/checkouts/{checkout}/delivery-areas/{delivery_area}/delivery-services",
            method=Method.GET,
        )
        return response


def validate_zip_code(zip_code: str | int):
    if len(re.findall(r"[^0-9]", str(zip_code))) > 0:
        raise ValueError(f"Invalid zip code: {zip_code}")


def validate_state_code(state_code: str | None):
    if state_code is not None:
        if len(state_code) != 2 or len(re.findall(r"[^A-z]+", state_code)) > 0:
            raise ValueError(f"Invalid state code: {state_code}")

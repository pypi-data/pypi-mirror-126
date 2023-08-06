from ikea_api.endpoints.cart.fragments import cart_props

cart = """
  query Cart(
    $languageCode: String
    ) {
    cart(languageCode: $languageCode) {
      ...CartProps
    }
  }
  %s
""" % (
    cart_props
)

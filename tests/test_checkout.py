from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_checkout(driver):

    login = LoginPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    login.login()

    product.add_to_cart()

    product.open_cart()

    cart.checkout()

    cart.fill_details()

    cart.finish_order()
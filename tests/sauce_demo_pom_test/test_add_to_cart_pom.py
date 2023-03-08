import time

from src.pages.cart_page import CartPage
from src.pages.list_products_page import ListProductsPage
from src.pages.login_page import LoginPage


def test_add_to_card(chrome_driver):
    # Init the pages for test this case
    login_page = LoginPage(chrome_driver)
    list_products_page = ListProductsPage(chrome_driver)
    cart_page = CartPage(chrome_driver)

    """LOGIN WITH VALID USER"""
    login_page.login_with_valid_user(username='standard_user', password='secret_sauce')

    """ADD PRODUCT TO CART"""
    list_products_page.add_product1_to_cart()
    list_products_page.click_to_open_cart_page()

    """CHECK PRODUCT IN CART"""
    cart_page.check_product1_in_cart()
    time.sleep(3)

from selenium.webdriver.common.by import By


class ListProductsPage:
    # Init driver for products list page
    def __init__(self, driver):
        self.driver = driver

    # Locators of products list page
    BTN_ADD_TO_CART_PRODUCT1 = (By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    CART_BTN = (By.ID, 'shopping_cart_container')

    # Interaction methods of product list page
    def click_to_open_cart_page(self):
        self.driver.find_element(*self.CART_BTN).click()

    def add_product1_to_cart(self):
        self.driver.find_element(*self.BTN_ADD_TO_CART_PRODUCT1).click()

    def click_product_detail(self, product_name):
        # Todo let implement it by yourself
        pass

    def sort_list_product(self, sort_by):
        # Todo let implement it by yourself
        pass

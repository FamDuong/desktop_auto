from selenium.webdriver.common.by import By


class CartPage:
    # Init driver for cart page
    def __init__(self, driver):
        self.driver = driver

    # Locators for cart page
    PRODUCT1_LOCATOR = (By.CSS_SELECTOR, 'a[id="item_4_title_link"] div')
    PRODUCT1_PRICE = (By.CSS_SELECTOR, 'div[class="inventory_item_price"]')
    PRODUCT1_DESCRIPTION = (By.CSS_SELECTOR, 'div[class="inventory_item_desc"]')

    # Interaction methods of cart page
    def open_page(self):
        self.driver.get('https://www.saucedemo.com/cart.html')

    def check_product1_in_cart(self):
        assert self.driver.find_element(*self.PRODUCT1_LOCATOR)
        assert self.driver.find_element(*self.PRODUCT1_LOCATOR).text == 'Sauce Labs Backpack'

    def get_price_product1(self) -> str:
        return self.driver.find_element(*self.PRODUCT1_PRICE).text

    def get_description_product1(self) -> str:
        return self.driver.find_element(*self.PRODUCT1_DESCRIPTION).text

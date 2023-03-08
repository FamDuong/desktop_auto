from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class LoginPage:

    # Init driver for login page
    def __init__(self, driver):
        self.driver = driver

    # Locators of login page
    USERNAME = (By.CSS_SELECTOR, 'input[data-test="username"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[data-test="password"]')
    BTN_LOGIN = (By.CSS_SELECTOR, 'input[data-test="login-button"]')
    TITLE_PRODUCT = (By.CSS_SELECTOR, 'span[class="title"]')
    ERROR_LOCKED_USER = (By.CSS_SELECTOR, 'h3[data-test="error"]')

    # Interaction methods of login page
    def open_page(self, url='https://www.saucedemo.com/'):
        self.driver.get(url)
        assert self.driver.title == 'Swag Labs'

    def enter_username(self, value_text):
        # get username locator
        username: WebElement = self.driver.find_element(*self.USERNAME)
        # Clear old value if any
        username.clear()
        # Set value to username
        username.send_keys(value_text)

    def enter_password(self, value):
        password: WebElement = self.driver.find_element(*self.PASSWORD)
        password.clear()
        password.send_keys(value)

    def click_btn_login(self):
        # Get button login locator
        btn_login: WebElement = self.driver.find_element(*self.BTN_LOGIN)
        # Click button login
        btn_login.click()

    def check_login_ok(self):
        # Get product title locator
        title_products: WebElement = self.driver.find_element(*self.TITLE_PRODUCT)

        # Verify the title 'Products' text is shown
        assert title_products.text == 'Products'

    def check_login_with_locked_user(self):
        # Get locator of error message
        error_message: WebElement = self.driver.find_element(*self.ERROR_LOCKED_USER)
        # Check error message
        assert error_message.text == 'Epic sadface: Sorry, this user has been locked out.'

    def login_with_valid_user(self, username, password):
        # Open login page
        self.open_page()
        # enter username & password
        self.enter_username(username)
        self.enter_password(password)
        # Click button login
        self.click_btn_login()

    def get_current_url(self) -> str:
        # To return the current url of the page
        return self.driver.current_url

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def test_valid_login(chrome_driver):
    """Enter the page"""
    chrome_driver.get('https://www.saucedemo.com/')
    assert chrome_driver.title == 'Swag Labs'

    # Locators
    username: WebElement = chrome_driver.find_element(By.CSS_SELECTOR, 'input[data-test="username"]')
    password: WebElement = chrome_driver.find_element(By.CSS_SELECTOR, 'input[data-test="password"]')
    login_btn: WebElement = chrome_driver.find_element(By.CSS_SELECTOR, 'input[data-test="login-button"]')

    # Interaction methods
    """Enter username & password"""

    username.clear()
    username.send_keys('standard_user')
    password.clear()
    password.send_keys('secret_sauce')
    # click login button
    login_btn.click()

    """Verify the title 'Products' is showed"""
    title_products: WebElement = chrome_driver.find_element(By.CSS_SELECTOR, 'span[class="title"]')
    assert title_products.text == 'Products'
    time.sleep(4)


def test_login_with_locked_user(chrome_driver):
    # Enter the page
    chrome_driver.get('https://www.saucedemo.com/')
    assert chrome_driver.title == 'Swag Labs'

    # Locators
    username: WebElement = chrome_driver.find_element(By.CSS_SELECTOR, 'input[data-test="username"]')
    password: WebElement = chrome_driver.find_element(By.CSS_SELECTOR, 'input[data-test="password"]')
    login_btn: WebElement = chrome_driver.find_element(By.CSS_SELECTOR, 'input[data-test="login-button"]')

    # Interaction methods
    # Enter username & password
    username.clear()
    username.send_keys('locked_out_user')
    password.clear()
    password.send_keys('secret_sauce')

    # click login button
    login_btn.click()

    error_message: WebElement = chrome_driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]')

    assert error_message.text == 'Epic sadface: Sorry, this user has been locked out.'


def test_with_no_username(chrome_driver):
    # Todo let implement it by yourself
    pass


def test_with_no_password(chrome_driver):
    # Todo let implement it by yourself
    pass

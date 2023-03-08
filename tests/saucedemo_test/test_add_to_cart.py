import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def test_add_to_card(chrome_driver):
    """LOGIN WITH VALID USER"""
    # Enter the page
    chrome_driver.get('https://www.saucedemo.com/')
    assert chrome_driver.title == 'Swag Labs'

    # Locators
    username: WebElement = chrome_driver.find_element(By.CSS_SELECTOR, 'input[data-test="username"]')
    password: WebElement = chrome_driver.find_element(By.CSS_SELECTOR, 'input[data-test="password"]')
    login_btn: WebElement = chrome_driver.find_element(By.CSS_SELECTOR, 'input[data-test="login-button"]')

    # Enter username & password
    username.clear()
    username.send_keys('standard_user')
    password.clear()
    password.send_keys('secret_sauce')

    # click login button
    login_btn.click()
    title_products: WebElement = chrome_driver.find_element(By.CSS_SELECTOR, 'span[class="title"]')
    # Verify the title 'Products' is shown
    assert title_products.text == 'Products'

    """SELECT A PRODUCT"""
    btn_add_2_cart_product1 = chrome_driver.find_element(By.CSS_SELECTOR,
                                                         'button[data-test="add-to-cart-sauce-labs-backpack"]')
    btn_add_2_cart_product1.click()

    """GO TO CART PAGE AND CHECK"""
    cart_icon: WebElement = chrome_driver.find_element(By.ID, 'shopping_cart_container')
    cart_icon.click()

    product1_name: WebElement = chrome_driver.find_element(By.CSS_SELECTOR, 'div[class="inventory_item_name"]')
    assert product1_name.text == 'Sauce Labs Backpack'

    time.sleep(5)

   
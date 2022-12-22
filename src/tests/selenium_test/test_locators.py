import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

from src.utils import chrome_driver_utils


def test_locators():
    # Init driver session for CocCoc
    options = ChromeOptions()
    options.binary_location = r'C:\Program Files\CocCoc\Browser\Application\browser.exe'
    chrome_driver_utils.install()
    driver = webdriver.Chrome(options=options)

    # Set implicit time waiting
    driver.implicitly_wait(10)

    # Get the page
    driver.get("https://demoqa.com/automation-practice-form")

    # Locators

    # By tag name
    title_form = driver.find_element(By.TAG_NAME, 'h5')

    # By ID
    first_name = driver.find_element(By.ID, 'firstName')

    # By CSS SELECTOR
    # CSS SELECTOR BY ID
    last_name = driver.find_element(By.CSS_SELECTOR, '#lastName')

    # CSS SELECTOR BY TAG + ATTRIBUTE
    email = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="name@example.com"]')

    # By Class:
    submit_btn = driver.find_element(By.CLASS_NAME, 'text-right col-md-2 col-sm-12')

    # Check title form
    assert 'Student Registration Form' == title_form.text

    # Enter first_name
    first_name.send_keys('selenium')
    # Enter last name
    last_name.send_keys('automation')

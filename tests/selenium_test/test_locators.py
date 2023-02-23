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
    # Check title form
    assert 'Student Registration Form' == title_form.text

    # By ID
    first_name = driver.find_element(By.ID, 'firstName')
    # Enter first_name
    first_name.send_keys('selenium')

    # By class name
    # by_class_name = driver.find_elements(By.CLASS_NAME, 'subjects-auto-complete__value-container subjects-auto-complete__value-container--is-multi css-1hwfws3')
    # assert by_class_name.


    # By CSS SELECTOR

    # CSS SELECTOR BY ID
    last_name = driver.find_element(By.CSS_SELECTOR, '#lastName')
    # Enter last name
    last_name.send_keys('automation')

    # CSS SELECTOR BY CLASS_NAME
    subjects = driver.find_element(By.CSS_SELECTOR, '.subjects-auto-complete__input')
    assert subjects.is_displayed()

    # CSS SELECTOR BY TAG + ATTRIBUTE value
    email = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="name@example.com"]')
    email.send_keys('john@doe.com')

    # CSS SELECTOR BY TAG + Chainable ATTRIBUTE value
    mobile_number = driver.find_element(By.CSS_SELECTOR, 'input[id="userNumber"][type="text"]')
    mobile_number.send_keys('0987654321')

    # CSS SELECTOR BY TAG + Class_name's value
    current_address = driver.find_element(By.CSS_SELECTOR, 'textarea.form-control')
    current_address.send_keys('Current Address')
    time.sleep(5)

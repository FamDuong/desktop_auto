import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_coccoc_search(coccoc_driver):
    # Access the coccoc search home page
    coccoc_driver.get('https://coccoc.com/search')

    # Enter the searching text and click to search

    search_box_locator = coccoc_driver.find_element(By.CSS_SELECTOR, 'input[class="suggestBox-K4SFm"]')
    search_box_locator.send_keys('tinhte' + Keys.RETURN)

    # Verify the text 'tinhte' appears
    search_result_locator = coccoc_driver.find_element(By.CSS_SELECTOR, 'div[class="newRightWiki-YyhNt"] div:nth-child(1)')
    assert 'Tinh Tế' == search_result_locator.text

    time.sleep(5)


def test_coccoc_search_2(coccoc_driver):
    # Access the coccoc search home page
    coccoc_driver.get('https://coccoc.com/search')

    # Enter the searching text and click to search

    search_box_locator = coccoc_driver.find_element(By.CSS_SELECTOR, 'input[class="suggestBox-K4SFm"]')
    search_box_locator.send_keys('coccoc' + Keys.RETURN)

    # Verify the text 'Cốc Cốc' appears
    search_result_locator = coccoc_driver.find_element(By.CSS_SELECTOR, 'div[class="newRightWiki-YyhNt"] div:nth-child(1)')
    assert 'Cốc Cốc' == search_result_locator.text

    time.sleep(5)

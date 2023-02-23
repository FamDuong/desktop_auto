import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

from src.utils import chrome_driver_utils


def test_search_by_coccoc():
    # Init driver session for CocCoc
    options = ChromeOptions()
    options.binary_location = r'C:\Program Files\CocCoc\Browser\Application\browser.exe'
    chrome_driver_utils.install()
    driver = webdriver.Chrome(options=options)

    # Set implicit time waiting
    driver.implicitly_wait(10)

    # Get the page
    driver.get("https://coccoc.com/search")

    # Get the title of the page and assert
    title = driver.title
    assert title == "Cốc Cốc"

    # Get element text box
    text_box = driver.find_element(by=By.CSS_SELECTOR, value="input.suggestBox-K4SFm")

    # Interact with element text box by entering the text and press to search
    text_box.send_keys("Cốc Cốc" + Keys.RETURN)

    # Verify the result, check the first results contain
    first_result = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[4]/div/div/ul/div[2]/h3/a/span')

    assert 'Cốc Cốc' in first_result.text
    time.sleep(1)

    driver.quit()


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Coccoc
from selenium.webdriver import ChromeOptions as CocCocOptions, Keys
from selenium.webdriver.chrome.service import Service as CocCocService


def test_first_test_open_chrome():
    # selenium 4
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://coccoc.com/search')
    driver.quit()


def test_search_by_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get('https://coccoc.com/search')
    box_search = driver.find_element(By.CSS_SELECTOR, 'input.suggestBox-K4SFm')
    box_search.send_keys('CocCoc' + Keys.RETURN)
    first_result = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[4]/div/div/ul/div[2]/h3/a/span')
    print(first_result.text)
    time.sleep(5)


def test_first_open_coccoc():

    coccoc_options = webdriver.ChromeOptions()
    coccoc_options.binary_location = '/Applications/CocCoc.app/Contents/MacOS/CocCoc'
    # coccoc_services = ChromeService(ChromeDriverManager().install())
    from webdriver_manager.core.utils import read_version_from_cmd, PATTERN
    # version = read_version_from_cmd(rf"/Applications/CocCoc.app/Contents/MacOS/CocCoc --version", PATTERN["CocCoc"])
    driver_binary = ChromeDriverManager(version='108.1.46.140').install()
    driver = webdriver.Chrome(executable_path=driver_binary, options=coccoc_options)
    # driver = webdriver.Chrome(service=coccoc_services, options=coccoc_options)
    driver.get('https://coccoc.com/search')

#
# def test_firefox():
#
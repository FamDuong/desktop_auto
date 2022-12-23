import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.core.utils import ChromeType

from src.utils import chrome_driver_utils


# Download chromedriver.exe then save to safe location, put its location to executable_path of ChromeService
# chromedriver.exe version should match with current CocCoc browser version
def test_init_coccoc_by_hard_coded_location():
    service = ChromeService(executable_path=r"C:\WebDriver\bin\chromedriver.exe")
    options = ChromeOptions()
    options.binary_location = r'C:\Program Files\CocCoc\Browser\Application\browser.exe'
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://google.com')
    time.sleep(5)
    driver.quit()


def test_init_coccoc_by_webdriver_manager():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    # service = ChromeService(executable_path=ChromeDriverManager(chrome_type=ChromeType.COCCOC).install())
    options = ChromeOptions()
    options.binary_location = r'C:\Program Files\CocCoc\Browser\Application\browser.exe'
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://google.com')
    time.sleep(5)
    driver.quit()


# Use custom service: chrome_driver_utils
def test_init_coccoc_by_other():
    options = ChromeOptions()
    options.binary_location = r'C:\Program Files\CocCoc\Browser\Application\browser.exe'
    chrome_driver_utils.install()
    driver = webdriver.Chrome(options=options)
    driver.get('https://google.com')
    time.sleep(5)
    driver.quit()

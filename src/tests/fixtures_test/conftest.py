import selenium.webdriver

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.core.utils import ChromeType

from src.utils import file_utils


@pytest.fixture()
def chrome_driver():
    # Init chrome driver
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Set implicit wait
    driver.implicitly_wait(10)

    # Return driver temporarily for using
    yield driver

    # Close the driver after test ( must use driver.quit() not driver.close())
    driver.quit()


@pytest.fixture()
def coccoc_driver():
    # Init coccoc driver
    service = ChromeService(executable_path=ChromeDriverManager(chrome_type=ChromeType.COCCOC).install())
    options = ChromeOptions()

    # options.binary_location = r'C:\Program Files\CocCoc\Browser\Application\browser.exe'
    if file_utils.check_file_is_exists(r'C:\Program Files\CocCoc\Browser\Application\browser.exe'):
        options.binary_location = r'C:\Program Files\CocCoc\Browser\Application\browser.exe'
    elif file_utils.check_file_is_exists(r'C:\Program Files (x86)\CocCoc\Browser\Application\browser.exe'):
        options.binary_location = r'C:\Program Files (x86)\CocCoc\Browser\Application\browser.exe'
    else:
        options.binary_location = r'C:\Users\taynq_coccoc\AppData\Local\CocCoc\Browser\Application\browser.exe'

    driver = webdriver.Chrome(service=service, options=options)

    # Set implicit wait
    driver.implicitly_wait(10)

    # maximize window
    # driver.maximize_window()

    # Return driver temporarily for using
    yield driver

    # Close the driver after test ( must use driver.quit() not driver.close())
    driver.quit()

import json

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CocCocOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as CocCocService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager

from src.utils import file_utils, os_utils


@pytest.fixture()
def chrome_driver():
    # Init chrome driver
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    # Set implicit wait
    driver.implicitly_wait(10)

    # Return driver temporarily for using
    yield driver

    # Close the driver after test ( must use driver.quit() not driver.close())
    driver.quit()


@pytest.fixture()
def coccoc_driver():
    # Init coccoc driver
    service = CocCocService(executable_path=ChromeDriverManager(chrome_type=ChromeType.COCCOC).install())
    options = CocCocOptions()

    # options.binary_location = r'C:\Program Files\CocCoc\Browser\Application\browser.exe'
    if file_utils.check_file_is_exists(r'C:\Program Files\CocCoc\Browser\Application\browser.exe'):
        options.binary_location = r'C:\Program Files\CocCoc\Browser\Application\browser.exe'
    elif file_utils.check_file_is_exists(r'C:\Program Files (x86)\CocCoc\Browser\Application\browser.exe'):
        options.binary_location = r'C:\Program Files (x86)\CocCoc\Browser\Application\browser.exe'
    else:
        options.binary_location = rf'C:\Users\{os_utils.get_username()}\AppData\Local\CocCoc\Browser\Application\browser.exe'

    driver = webdriver.Chrome(service=service, options=options)

    # Set implicit wait
    driver.implicitly_wait(10)

    # maximize window
    # driver.maximize_window()

    # Return driver temporarily for using
    yield driver

    # Close the driver after test ( must use: driver.quit(), dont use: driver.close())
    driver.quit()


@pytest.fixture
def config(scope='session'):
    # Read the file
    with open('../../config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome', 'CocCoc']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config
    return config


@pytest.fixture()
def web_driver(config):
    if config['browser'] == 'Firefox':
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif config['browser'] == 'Chrome':
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif config['browser'] == 'CocCoc':
        service = CocCocService(executable_path=ChromeDriverManager(chrome_type=ChromeType.COCCOC).install())
        options = CocCocOptions()

        # options.binary_location = r'C:\Program Files\CocCoc\Browser\Application\browser.exe'
        if file_utils.check_file_is_exists(r'C:\Program Files\CocCoc\Browser\Application\browser.exe'):
            options.binary_location = r'C:\Program Files\CocCoc\Browser\Application\browser.exe'
        elif file_utils.check_file_is_exists(r'C:\Program Files (x86)\CocCoc\Browser\Application\browser.exe'):
            options.binary_location = r'C:\Program Files (x86)\CocCoc\Browser\Application\browser.exe'
        else:
            options.binary_location = rf'C:\Users\{os_utils.get_username()}\AppData\Local\CocCoc\Browser\Application\browser.exe'

        driver = webdriver.Chrome(service=service, options=options)

    else:
        raise Exception(f"Browser {config['browser']} is not supported")

    driver.implicitly_wait(config['implicit_wait'])

    yield driver

    driver.quit()

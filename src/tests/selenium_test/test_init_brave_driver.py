import time


from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options as ChromeOptions

from src.utils import file_utils, os_utils


# Download chromedriver.exe then save to safe location, put its location to executable_path of ChromeService
# chromedriver.exe version should match with current Chrome browser version
def test_init_brave_by_hard_coded_location():
    options = ChromeOptions()
    # options.binary_location = r'C:\Users\taynq_coccoc\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe'
    # options.binary_location = rf'C:\Users\{os_utils.get_username()}\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe'

    if file_utils.check_file_is_exists(r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'):
        options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
    else:
        options.binary_location = r'C:\Users\taynq_coccoc\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe'

    service = ChromeService(executable_path=r"C:\WebDriver\bin\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://google.com')
    time.sleep(5)
    driver.quit()


# pip3 install webdriver-manager
def test_init_brave_by_webdriver_manager():
    options = ChromeOptions()
    # options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
    options.binary_location = rf'C:\Users\{os_utils.get_username()}\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe'
    # if file_utils.check_file_is_exists(r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'):
    #     options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
    # else:
    #     options.binary_location = r'C:\Users\taynq_coccoc\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe'
    driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()), options=options)
    driver.get('https://google.com')
    time.sleep(5)
    driver.quit()

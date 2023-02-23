import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


# Download geckodriver.exe then save to safe location, put its location to executable_path of FirefoxService
# geckodriver.exe version should match with current firefox browser version
def test_init_firefox_by_hard_coded_location():
    service = FirefoxService(executable_path=r"C:\WebDriver\gecko_driver\geckodriver.exe")
    driver = webdriver.Firefox(service=service)
    driver.get('https://google.com')
    time.sleep(5)
    driver.quit()


# pip3 install webdriver-manager
def test_init_firefox_by_webdriver_manager():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get('https://google.com')
    time.sleep(5)
    driver.quit()

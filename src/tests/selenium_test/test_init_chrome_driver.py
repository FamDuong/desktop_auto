import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


# Download chromedriver.exe then save to safe location, put its location to executable_path of ChromeService
# chromedriver.exe version should match with current Chrome browser version
def test_init_chrome_by_hard_coded_location():
    service = ChromeService(executable_path=r"C:\WebDriver\bin\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get('https://google.com')
    time.sleep(5)
    driver.quit()


# pip3 install webdriver-manager
def test_init_chrome_by_webdriver_manager():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('https://google.com')
    time.sleep(5)
    driver.quit()

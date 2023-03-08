import time

from src.pages.login_page import LoginPage


def test_valid_login_page(chrome_driver):
    # Init login page
    login_page = LoginPage(chrome_driver)

    # Open login page
    login_page.open_page()

    # enter username
    login_page.enter_username('standard_user')

    # enter password
    login_page.enter_password('secret_sauce')

    # click button login
    login_page.click_btn_login()

    # request automation script to verify login ok
    login_page.check_login_ok()
    # print(login_page.get_current_url())
    assert login_page.get_current_url() == 'https://www.saucedemo.com/inventory.html'

    time.sleep(4)


def test_login_with_locked_user(chrome_driver):
    # Init the login page object
    login_page = LoginPage(chrome_driver)

    # Open login page
    login_page.open_page()
    login_page.enter_username('locked_out_user')
    login_page.enter_password('secret_sauce')
    login_page.click_btn_login()

    # Verify error locked user shown:
    login_page.check_login_with_locked_user()

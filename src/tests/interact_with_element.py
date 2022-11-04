import time

from pywinauto import Application


def open_coccoc_install_dialog(file_name='CocCocSetup.exe'):
    # Start file setup
    try:
        Application(backend='uia').start(f'C:\\Users\\taynq_coccoc\\Downloads\\{file_name}',
                                         retry_interval=2, timeout=30)
    except Exception as e:
        print(e)


# connect to the opening window
def connect_to_opening_window():
    # Open installing dialog
    open_coccoc_install_dialog()
    # Start file setup
    try:
        app = Application(backend="uia").connect(
            class_name="#32770",
            control_type=50033,
            title_re='Initializing..., Cốc Cốc Installer',
            timeout=30)
        return app.window(title_re='Initializing..., Cốc Cốc Installer')
    except Exception as e:
        print(e)


def test_click_element():
    dialog = connect_to_opening_window()
    dialog.child_window(auto_id="1", control_type="Button").click()


def close_dialog(dialog=None):
    # Open installing dialog
    if dialog is None:
        dialog = connect_to_opening_window()
    # Click to close
    dialog.child_window(auto_id="1", control_type="Button").click()
    # Click button "Cancel installation"
    dialog.child_window(auto_id="2", control_type="Button").click()


def test_close_dialog():
    close_dialog()


# Check exist element
def test_check_exist():
    dialog = connect_to_opening_window()
    dialog.print_control_identifiers()
    assert dialog.child_window(title="Install", auto_id="2024", control_type="Button").exists()
    close_dialog(dialog)


# get text of element
def test_get_text():
    dialog = connect_to_opening_window()
    # dialog.print_control_identifiers()
    text = dialog.child_window(auto_id="2025", control_type="CheckBox")
    print(text)
    close_dialog(dialog)


# Set text
def test_set_text():
    app = None
    try:
        app = Application(backend='uia').start(rf'C:\Program Files\CocCoc\Browser\Application\browser.exe',
                                               retry_interval=2, timeout=30)
        time.sleep(2)
    except Exception as e:
        print(e)
    app.window(title_re='New Tab').set_focus()
    app.window().child_window(title_re='Address and search bar',
                              control_type=50004).wait('visible', timeout=10).type_keys('https://google.com{ENTER}')
    time.sleep(2)
    app.window().close()





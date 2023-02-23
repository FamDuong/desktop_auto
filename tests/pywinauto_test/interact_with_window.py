# Start then connect to it
import time

from pywinauto import Application


def get_window_title(file_name='CocCocSetup.exe'):
    # Start file setup
    try:
        Application(backend='uia').start(f'C:\\Users\\taynq_coccoc\\Downloads\\{file_name}',
                                                  retry_interval=2, timeout=30)
        # dialog.window().print_control_identifiers()
        app = Application(backend="uia").connect(
            # class_name="#32770",
            # control_type=50033,
            title_re='Initializing..., Cốc Cốc Installer',
            timeout=30)
        print(app.window(title_re='Initializing..., Cốc Cốc Installer').window_text())
        # return app.window()
    except Exception as e:
        print(e)


def test_get_window_title():
    get_window_title()


def check_window_exist(file_name='CocCocSetup.exe'):
    # Start file setup
    try:
        Application(backend='uia').start(f'C:\\Users\\taynq_coccoc\\Downloads\\{file_name}',
                                                  retry_interval=2, timeout=30)
        # dialog.window().print_control_identifiers()
        app = Application(backend="uia").connect(
            # class_name="#32770",
            # control_type=50033,
            title_re='Initializing..., Cốc Cốc Installer',
            timeout=30)
        print(app.window(title_re='Initializing..., Cốc Cốc Installer').is_visible())
        print(app.window(title_re='Initializing..., Cốc Cốc Installer').exists())
        # return app.window()
    except Exception as e:
        print(e)


def test_check_window_exist():
    check_window_exist()


# Maximize
def maximize_window():
    app = None
    try:
        app = Application(backend='uia').start(rf'C:\Program Files\CocCoc\Browser\Application\browser.exe',
                                               retry_interval=2, timeout=30)
        time.sleep(2)
    except Exception as e:
        print(e)
    app.window(title_re='New Tab').set_focus()
    app.window(title_re='New Tab').maximize()


def test_maximize_window():
    maximize_window()

import time

from pywinauto import Application


def open_coccoc_install_dialog(file_name='CocCocSetup.exe'):
    # Start file setup
    try:
        dialog = Application(backend='uia').start(f'C:\\Users\\taynq_coccoc\\Downloads\\{file_name}',
                                                  retry_interval=2, timeout=30)
        # dialog.window().print_control_identifiers()
        app = Application(backend="uia").connect(
            class_name="#32770",
            control_type=50033,
            title_re='Initializing..., Cốc Cốc Installer',
            timeout=30)
        app.window().print_control_identifiers()
    except Exception as e:
        print(e)


def test_print_control_identifier():
    open_coccoc_install_dialog()


def test_print_control_identifier2():
    app = None
    try:
        app = Application(backend='uia').start(rf'C:\Program Files\CocCoc\Browser\Application\browser.exe',
                                         retry_interval=2, timeout=30)
        time.sleep(2)
    except Exception as e:
        print(e)
    coccoc_window = app.window(title_re='New Tab')
    coccoc_window.print_control_identifiers()
    time.sleep(1)
    coccoc_window.close()

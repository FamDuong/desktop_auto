
from pywinauto import Application


def open_coccoc_install_dialog(file_name='CocCocSetup.exe'):
    # Start file setup
    try:
        Application(backend='uia').start(f'C:\\Users\\taynq\\Downloads\\{file_name}',
                                         retry_interval=2, timeout=30)
    except Exception as e:
        print(e)


def test_open_coccoc_install_dialog():
    open_coccoc_install_dialog()


def open_install_dialog(file_name='CocCocSetup.exe'):
    # Start file setup
    try:
        Application(backend='uia').start(f'C:\\Users\\taynq\\Downloads\\{file_name}',
                                         retry_interval=2, timeout=30)
    except Exception as e:
        print(e)


def test_open_install_dialog():
    open_install_dialog()
    
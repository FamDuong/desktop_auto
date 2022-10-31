
from pywinauto import Application


def open_coccoc():
    # Start the executable file
    try:
        Application(backend='uia').start(rf'C:\Program Files\CocCoc\Browser\Application\browser.exe',
                                         retry_interval=2, timeout=30)
    except Exception as e:
        print(e)


def test_open_coccoc_install_dialog():
    open_coccoc()


def start_program(executable_path=None):
    # Start the executable file
    try:
        Application(backend='uia').start(executable_path,
                                         retry_interval=2, timeout=30)
    except Exception as e:
        print(e)


def test_start_program():
    start_program(executable_path=r'C:\Program Files (x86)\Notepad++\notepad++.exe')




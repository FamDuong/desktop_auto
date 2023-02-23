import os
import time
import psutil
from pywinauto import Application

"""Connecting to the window"""


# Start then connect to it
def open_then_connect_to_window(file_name='CocCocSetup.exe'):
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
        print(app.window())
        # return app.window()
    except Exception as e:
        print(e)


def test_open_then_connect_to_window():
    open_then_connect_to_window()


# connect to the opening window
def connect_to_opening_window():
    # Start file setup
    try:
        app = Application(backend="uia").connect(
            class_name="#32770",
            control_type=50033,
            title_re='Initializing..., Cốc Cốc Installer',
            timeout=30)
        # print(app.window())
        return app
    except Exception as e:
        print(e)


def test_connect_to_opening_window():
    connect_to_opening_window()


"""Closing the window"""


def close_window_by_kill():
    open_then_connect_to_window()
    window = connect_to_opening_window()
    window.kill()


def test_close_window():
    close_window_by_kill()


# Closing the window
def close_window_by_title():
    # open_then_connect_to_window()
    # time.sleep(1)
    app = None
    try:
        app = Application(backend='uia').start(rf'C:\Program Files\CocCoc\Browser\Application\browser.exe',
                                         retry_interval=2, timeout=30)
        time.sleep(3)
    except Exception as e:
        print(e)
    app.window(title_re='New Tab').close()


def test_close_window_by_title():
    close_window_by_title()


# Close by sendkeys
def close_window_by_send_key():
    app = None
    try:
        app = Application(backend='uia').start(rf'C:\Program Files\CocCoc\Browser\Application\browser.exe',
                                         retry_interval=2, timeout=30)
        time.sleep(3)
    except Exception as e:
        print(e)

    app.window(title_re='New Tab').type_keys("%{F4}")


def test_close_window_by_send_key():
    close_window_by_send_key()


"""Close window by process_id, process_name"""


def get_running_processes(process_name):
    list_of_process_objects = []
    for proc in psutil.process_iter():
        try:
            process_info = proc.as_dict(attrs=['pid', 'name'])
            if process_name.lower() in process_info['name'].lower():
                list_of_process_objects.append(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    if len(list_of_process_objects) > 0:
        process_ids = []
        for process in list_of_process_objects:
            process_ids.append(process['pid'])

        return process_ids


def test_get_running_process():
    print(get_running_processes(process_name='browser.exe'))


def test_close_window_by_id():
    try:
        Application(backend='uia').start(rf'C:\Program Files\CocCoc\Browser\Application\browser.exe',
                                               retry_interval=2, timeout=30)
        time.sleep(2)
    except Exception as e:
        print(e)
    pids = get_running_processes('browser.exe')
    while len(pids) > 0:
        for pid in pids:
            os.system(f'taskkill /PID {pid} /F ')


# close by process_name
def close_by_process_name(process_name):
    cmd = rf'taskkill /IM {process_name} /F'
    os.system(cmd)


def test_close_by_process_name():
    try:
        Application(backend='uia').start(rf'C:\Program Files\CocCoc\Browser\Application\browser.exe',
                                         retry_interval=2, timeout=30)
        time.sleep(2)
    except Exception as e:
        print(e)
    close_by_process_name(process_name='browser.exe')

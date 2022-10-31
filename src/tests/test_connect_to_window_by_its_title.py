from pywinauto import Application


# Start then connect to it
def open_then_connect_to_window(file_name='CocCocSetup.exe'):
    # Start file setup
    try:
        Application(backend='uia').start(f'C:\\Users\\taynq\\Downloads\\{file_name}',
                                                  retry_interval=2, timeout=30)
        # dialog.window().print_control_identifiers()
        app = Application(backend="uia").connect(
            # class_name="#32770",
            # control_type=50033,
            title_re='Initializing..., Cốc Cốc Installer',
            timeout=30)
        print(app.window())
    except Exception as e:
        print(e)


def test_open_then_connect_to_window():
    open_then_connect_to_window()


# connect to the opening window
def connect_to_opening_window(file_name='CocCocSetup.exe'):
    # Start file setup
    try:
        app = Application(backend="uia").connect(
            # class_name="#32770",
            # control_type=50033,
            title_re='Initializing..., Cốc Cốc Installer',
            timeout=30)
        print(app.window())
    except Exception as e:
        print(e)


def test_connect_to_opening_window():
    connect_to_opening_window()

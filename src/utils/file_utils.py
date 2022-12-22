# To get project root directory
import os
from pathlib import Path


def get_project_root() -> Path:
    # print(Path(__file__).parent.parent)
    return Path(__file__).parent.parent


def test_get_project_root():
    print(get_project_root())


# To check the folder is existed or not
def check_folder_is_exists(directory_with_path):
    if os.path.isdir(directory_with_path):
        return True
    else:
        return False

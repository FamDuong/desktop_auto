# To get project root directory
from pathlib import Path


def get_project_root() -> Path:
    # print(Path(__file__).parent.parent)
    return Path(__file__).parent.parent


def test_get_project_root():
    print(get_project_root())
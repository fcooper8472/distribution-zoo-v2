from streamlit.testing.v1 import AppTest
from pathlib import Path

import pytest

app_file_path = Path(__file__).resolve().parent.parent / 'main.py'
assert app_file_path.is_file()


@pytest.fixture
def app_test() -> AppTest:
    return AppTest.from_file(script_path=str(app_file_path), default_timeout=100.0).run()


@pytest.fixture(scope='session')
def at_normal() -> AppTest:
    at = AppTest.from_file(script_path=str(app_file_path), default_timeout=100.0).run()
    at.sidebar.selectbox(key='dist_class').select('Continuous Univariate').run()
    at.sidebar.selectbox(key='dist').select('Normal').run()

    assert at.main.header[0].value == 'Normal distribution'

    return at


def get_test_output_dir():
    return Path(__file__).parent / 'test_output'

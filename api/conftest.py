import pytest
from selenium import webdriver

from utils.api_method import ReqresApi


@pytest.fixture(scope="function")
def api():
    return ReqresApi('https://reqres.in')

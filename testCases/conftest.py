from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as firefoxService
import pytest

@pytest.fixture()
def setup():
    # service = firefoxService(executable_path=GeckoDriverManager().install())
    # return webdriver.Firefox(service=service)
    return webdriver.Chrome()
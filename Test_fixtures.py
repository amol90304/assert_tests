import pytest
from selenium import webdriver


driver = None


@pytest.fixture
def Setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    print(driver.title)
    driver.close()


def test1(Setup):
    driver.get("https://google.com")

def test2(Setup):
    driver.get("https://facebook.com")

def test3(Setup):
    driver.get("https://linkedin.com")






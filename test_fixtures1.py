import pytest
from selenium import webdriver

driver = None


@pytest.fixture
def setup1():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    print(driver.title)
    driver.minimize_window()
    driver.close()



def test_demo1(setup1):
    driver.get("https://google.com")

def test_demo2(setup1):
    driver.get("https://facebook.com")

def test_demo3(setup1):
    driver.get("https://amazon.com")










import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome(executable_path='./tests/chromedriver_83')
    yield driver
    driver.quit()

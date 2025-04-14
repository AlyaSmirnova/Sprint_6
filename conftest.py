import pytest
from selenium import webdriver
from src.config import Config

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Config.URL)
    yield driver
    driver.quit()


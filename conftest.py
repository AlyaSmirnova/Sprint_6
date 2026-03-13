import pytest
from selenium import webdriver
from src.config import Config
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(Config.URL)
    yield driver
    driver.quit()


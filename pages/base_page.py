from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.config import Config
import allure
from src.locators import OrderPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Navigate to the base URL')
    def navigate(self):
        with allure.step(f'Opening URL: {Config.URL}'):
            self.driver.get(Config.URL)

    @allure.step('Wait for element visibility: {locator}')
    def wait_for_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator), message = f'Element {locator} not found within {timeout} seconds')

    @allure.step('Scroll to element: {locator}')
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Click on element: {locator}')
    def click_element(self, locator):
        self.wait_for_element(locator).click()

    @allure.step('Retrieve text from element: {locator}')
    def get_element_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step('Input text "{keys}" into field: {locator}')
    def input_text(self, locator, keys):
        self.wait_for_element(locator).send_keys(keys)

    @allure.step('Select option "{option_text}" from dropdown {dropdown_locator}')
    def select_dropdown_option(self, dropdown_locator, option_text):
        self.click_element(dropdown_locator)
        option_locator = (OrderPageLocators.RENTAL_OPTION[0], OrderPageLocators.RENTAL_OPTION[1].format(option_text))
        self.click_element(option_locator)

    @allure.step('Get current page URL')
    def get_current_url(self):
        return self.driver.current_url

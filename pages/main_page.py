from pages.base_page import BasePage
from src.locators import MainPageLocators
import allure


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Click the "Order" button in the header')
    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step('Scroll to bottom and click the footer "Order" button')
    def click_order_button_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        element = self.wait_for_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Verify visibility of all "Order" buttons')
    def verify_order_buttons_visible(self):
        with allure.step('Checking header Order button'):
            assert self.wait_for_element(MainPageLocators.ORDER_BUTTON_TOP).is_displayed()
        with allure.step('Checking footer Order button'):
            assert self.wait_for_element(MainPageLocators.ORDER_BUTTON_BOTTOM).is_displayed()

    @allure.step('Click on the "Scooter" logo')
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Click on the "Yandex" logo')
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

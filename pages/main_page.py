from pages.base_page import BasePage
from src.locators import MainPageLocators
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_order_button_top(self):
        with allure.step("Нажать кнопку 'Заказать' вверху страницы"):
            self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        with allure.step("Нажать кнопку 'Заказать' внизу страницы"):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def verify_order_buttons_visible(self):
        with allure.step("Проверить наличие кнопок 'Заказать'"):
            assert self.wait_for_element(MainPageLocators.ORDER_BUTTON_TOP)
            assert self.wait_for_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        with allure.step("Кликнуть на логотип Самокат"):
            self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        with allure.step("Кликнуть на логотип Яндекс"):
            self.click_element(MainPageLocators.YANDEX_LOGO)
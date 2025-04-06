from src.locators import OrderPageLocators
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_order_page_opened(self):
        with allure.step("Проверить, что открыта страница заказа"):
            assert self.wait_for_element(OrderPageLocators.ORDER_HEADER)
            assert "order" in self.driver.current_url

    def fill_personal_info(self, first_name, last_name, address, metro_station, phone):
        with allure.step("Заполнить форму с личной информацией"):
            self.input_text(OrderPageLocators.FIRST_NAME, first_name)
            self.input_text(OrderPageLocators.LAST_NAME, last_name)
            self.input_text(OrderPageLocators.ADDRESS, address)
            self.click_element(OrderPageLocators.METRO_STATION)
            metro_locator = (OrderPageLocators.METRO_STATION[0], OrderPageLocators.METRO_STATION[1].format(metro_station))
            self.click_element(metro_locator)
            self.input_text(OrderPageLocators.PHONE, phone)
            self.click_element(OrderPageLocators.BUTTON_NEXT)

    def fill_rental_info(self, date, rental_time, color, comment):
        with allure.step("Заполнить форму с деталями заказа самоката"):
            self.input_text(OrderPageLocators.DATE, date)
            self.select_dropdown_option(OrderPageLocators.RENTAL_TIME, rental_time)
            color_locator = (OrderPageLocators.COLOR[0], OrderPageLocators.COLOR[1].format(color))
            self.click_element(color_locator)
            self.input_text(OrderPageLocators.COMMENT, comment)
            self.click_element(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        with allure.step("Нажать кнопку подтверждения заказа"):
            self.click_element(OrderPageLocators.CONFIRMATION_BUTTON)

    def check_success_message(self):
        with allure.step("Проверить наличие всплываающего окна с сообщением об успешном оформлении заказа"):
            success_message = self.wait_for_element(OrderPageLocators.SUCCESS_MESSAGE)
            assert "Заказ оформлен" in success_message.text
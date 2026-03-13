from src.locators import OrderPageLocators
from pages.base_page import BasePage
import allure
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Verify the Order page is opened')
    def verify_order_page_opened(self):
        with allure.step('Checking header and URL for "order" keyword'):
            assert self.wait_for_element(OrderPageLocators.ORDER_HEADER)
            assert "order" in self.driver.current_url

    @allure.step('Fill personal information: {first_name} {last_name}')
    def fill_personal_info(self, first_name, last_name, address, metro_station, phone):
        self.input_text(OrderPageLocators.FIRST_NAME, first_name)
        self.input_text(OrderPageLocators.LAST_NAME, last_name)
        self.input_text(OrderPageLocators.ADDRESS, address)
        with allure.step(f'Selecting metro station: {metro_station}'):
            self.click_element(OrderPageLocators.METRO_STATION)
            metro_locator = (OrderPageLocators.METRO_OPTION[0], OrderPageLocators.METRO_OPTION[1].format(metro_station))
            self.scroll_to_element(metro_locator)
            self.click_element(metro_locator)
        self.input_text(OrderPageLocators.PHONE, phone)
        self.click_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Fill rental details: date={date}, duration={rental_time}')
    def fill_rental_info(self, date, rental_time, color, comment):
        with allure.step(f'Enter date: {date}'):
            date_field = self.wait_for_element(OrderPageLocators.DATE)
            date_field.send_keys(date)
            date_field.send_keys(Keys.ENTER)
        self.select_dropdown_option(OrderPageLocators.RENTAL_TIME, rental_time)
        with allure.step(f'Selecting scooter color: {color}'):
            color_locator = (OrderPageLocators.COLOR[0], OrderPageLocators.COLOR[1].format(color))
            self.click_element(color_locator)
        self.input_text(OrderPageLocators.COMMENT, comment)
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Confirm the order in the modal window')
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRMATION_BUTTON)

    @allure.step('Verify "Order Success" message appears')
    def check_success_message(self):
        success_message = self.wait_for_element(OrderPageLocators.SUCCESS_MESSAGE)
        assert "Заказ оформлен" in success_message.text

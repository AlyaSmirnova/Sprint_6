import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
import allure


@allure.feature('Order Placement Functionality')
class TestOrderPage:

    # Test data remains in Russian to match the service localization requirements
    TEST_DATA = [
        (
            "Алина",
            "Смирнова",
            "Санкт-Петербург, ул. Миллионная, д. 6",
            "Черкизовская",
            "89111173452",
            "25.05.2026",
            "двое суток",
            "black",
            "Позвонить за полчаса"
        ),
        (
            "Илья",
            "Громов",
            "Москва, ул. Ярцевская, д. 17",
            "Сокольники",
            "89546738265",
            "17.06.2026",
            "сутки",
            "grey",
            "Не звонить перед приездом"
        )
    ]

    @allure.title('Successful scooter order: {first_name} {last_name}')
    @allure.description('Verify that a user can complete the full order flow with various data sets')
    @pytest.mark.parametrize("first_name, last_name, address, metro_station, phone, date, rental_time, color, comment", TEST_DATA)
    def test_order_page(self, driver, first_name, last_name, address, metro_station, phone, date, rental_time, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        with allure.step('Step 1: Navigate to the application and start ordering'):
            main_page.navigate()
            main_page.click_order_button_top()
        with allure.step(f'Step 2: Fill personal information for {first_name}'):
            order_page.fill_personal_info(first_name, last_name, address, metro_station, phone)
        with allure.step('Step 3: Fill rental details and submit'):
            order_page.fill_rental_info(date, rental_time, color, comment)
            order_page.confirm_order()
        with allure.step('Step 4: Verify the success confirmation modal'):
            order_page.check_success_message()

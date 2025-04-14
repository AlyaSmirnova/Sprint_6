import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
import allure


@allure.feature("Тестирование раздела оформления заказа")
class TestOrderPage:
    TEST_DATA = [
        (
            "Алина",
            "Смирнова",
            "Санкт-Петербург, ул. Миллионная, д. 6",
            "Черкизовская",
            "89111173452",
            "25.05.2025",
            "двое суток",
            "black",
            "Позвонить за полчаса"
        ),
        (
            "Илья",
            "Громов,"
            "Москва, ул. Ярцевская, д. 17",
            "Сокольники",
            "89546738265",
            "17.06.2025",
            "одни сутки",
            "grey",
            "Не звонить перед приездом"
        )
    ]

    @pytest.mark.parametrize("first_name, last_name, address, metro_station, phone, date, rental_time, color, comment", TEST_DATA)

    def test_order_page(self, driver, first_name, last_name, address, metro_station, phone, date, rental_time, color, comment):
        with allure.step("Проверить успешное оформление заказа с 2-мя разными наборами тестовых данных"):
            main_page = MainPage(driver)
            order_page = OrderPage(driver)
            main_page.navigate()
            main_page.click_order_button_top()
            order_page.fill_personal_info(first_name, last_name, address, metro_station, phone)
            order_page.fill_rental_info(date, rental_time, color, comment)
            order_page.confirm_order()
            order_page.check_success_message()
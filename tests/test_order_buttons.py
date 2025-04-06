from pages.main_page import MainPage
from pages.order_page import OrderPage
from src.config import Config
import allure


@allure.feature("Тестирование кнопок 'Заказать'")
def test_order_button_top(driver):
    with allure.step("Проверить переход на страницу заказа самоката через кнопку 'Заказать' вверху страницы"):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        driver.get(Config.URL)
        main_page.verify_order_buttons_visible()
        main_page.click_order_button_top()
        order_page.verify_order_page_opened()

def test_order_button_bottom(driver):
    with allure.step("Проверить переход на страницу заказа самоката через кнопку 'Заказать' внизу страницы"):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        driver.get(Config.URL)
        main_page.verify_order_buttons_visible()
        main_page.click_order_button_bottom()
        order_page.verify_order_page_opened()
from pages.main_page import MainPage
from pages.order_page import OrderPage
from src.config import Config
import allure


@allure.feature('Order Navigation Flow')
class TestOrderNavigation:

    @allure.title('Navigate to Order Page via Header Button')
    @allure.description('Verify that clicking the "Order" button in the header redirects the user to the Order form')
    def test_order_button_top(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        with allure.step(f'Open application URL: {Config.URL}'):
            driver.get(Config.URL)
        with allure.step('Verify and click the "Order" button in the header'):
            main_page.verify_order_buttons_visible()
            main_page.click_order_button_top()
        with allure.step('Verify redirection to the Order Page'):
            order_page.verify_order_page_opened()

    @allure.title('Navigate to Order Page via Footer Button')
    @allure.description('Verify that scrolling down and clicking the "Order" button at the bottom redirects to the Order form')
    def test_order_button_bottom(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        with allure.step(f'Open application URL: {Config.URL}'):
            driver.get(Config.URL)
        with allure.step('Verify and click the "Order" button at the bottom'):
            main_page.verify_order_buttons_visible()
            main_page.click_order_button_bottom()
        with allure.step('Verify redirection to the Order Page'):
            order_page.verify_order_page_opened()

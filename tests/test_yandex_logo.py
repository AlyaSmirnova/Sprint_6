from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.feature("Тестирование перехода на страницу Яндекс.Дзен")
def test_yandex_logo_redirects_to_dzen(driver):
    with allure.step("Проверить переход на страницу Яндекс.Дзен при нажатии на лого яндекса"):
        main_page = MainPage(driver)
        main_page.navigate()
        main_page.click_yandex_logo()
        WebDriverWait(driver, timeout=15).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in main_page.get_current_url()
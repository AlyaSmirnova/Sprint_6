from pages.main_page import MainPage
import allure


@allure.feature("Тестирование перехода на страницу Яндекс.Самокат")
def test_scooter_logo_redirects_to_main_page(driver):
    with allure.step("Проверить переход на главную страницу Яндекс.Самокат при нажатии на лого самоката"):
        main_page = MainPage(driver)
        main_page.navigate()
        main_page.click_scooter_logo()
        assert "qa-scooter.praktikum-services.ru" in main_page.get_current_url()
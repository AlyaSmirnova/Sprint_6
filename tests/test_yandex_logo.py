from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.feature("Logo Navigation")
class TestLogoNavigation:

    @allure.title('Redirect to Yandex Dzen via "Yandex" Logo')
    @allure.description('Verify that clicking the "Yandex" logo opens the Dzen page in a new tab')
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        with allure.step('Step 1: Open the application'):
            main_page.navigate()
        with allure.step('Step 2: Click on the "Yandex" logo'):
            main_page.click_yandex_logo()
        with allure.step('Step 3: Switch to the newly opened browser tab'):
            WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
            new_window = driver.window_handles[1]
            driver.switch_to.window(new_window)
            WebDriverWait(driver, 15).until(EC.url_contains("dzen.ru"))
        with allure.step('Step 4: Verify redirection to Dzen.ru'):
            assert "dzen.ru" in main_page.get_current_url(), f'Expected Dzen URL, but got: {current_url}'

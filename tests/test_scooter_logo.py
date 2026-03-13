from pages.main_page import MainPage
import allure


@allure.feature('Logo Navigation')
class TestLogoNavigation:

    @allure.title('Redirect to Main Page via "Scooter" Logo')
    @allure.description('Verify that clicking the "Scooter" logo redirects the user back to the service home page')
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)
        with allure.step('Step 1: Open the application and navigate away from the home page'):
            main_page.navigate()
        with allure.step('Step 2: Click on the "Scooter" logo'):
            main_page.click_scooter_logo()
        with allure.step('Step 3: Verify redirection to the base URL'):
            assert "qa-scooter.praktikum-services.ru" in main_page.get_current_url(), f'Expected home page URL, but got: {current_url}'

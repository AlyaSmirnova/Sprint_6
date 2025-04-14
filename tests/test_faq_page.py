from pages.faq_page import FAQPage
from src.locators import FAQLocators
import allure


@allure.feature("Тестирование раздела 'Вопросы о важном'")
class TestFaqPage:
    def test_get_answer_to_question_1(self, driver):
        with allure.step('Проверка ответа на вопрос 1'):
            faq_page = FAQPage(driver)
            faq_page.open_page()
            faq_page.check_faq_section_title()
            faq_page.scroll_to_faq_section()
            faq_page.click_question(FAQLocators.QUESTION_1)
            actual_answer = faq_page.get_answer_text(FAQLocators.ANSWER_1)
            expected_answer = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
            assert actual_answer == expected_answer, f"Ошибка. Ожидали: {expected_answer}, а получили: {actual_answer}"
    def test_get_answer_to_question_2(self, driver):
        with allure.step('Проверка ответа на вопрос 2'):
            faq_page = FAQPage(driver)
            faq_page.open_page()
            faq_page.check_faq_section_title()
            faq_page.scroll_to_faq_section()
            faq_page.click_question(FAQLocators.QUESTION_2)
            actual_answer = faq_page.get_answer_text(FAQLocators.ANSWER_2)
            expected_answer = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
            assert actual_answer == expected_answer, f"Ошибка. Ожидали: {expected_answer}, а получили: {actual_answer}"
    def test_get_answer_to_question_3(self, driver):
        with allure.step('Проверка ответа на вопрос 3'):
            faq_page = FAQPage(driver)
            faq_page.open_page()
            faq_page.check_faq_section_title()
            faq_page.scroll_to_faq_section()
            faq_page.click_question(FAQLocators.QUESTION_3)
            actual_answer = faq_page.get_answer_text(FAQLocators.ANSWER_3)
            expected_answer = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
            assert actual_answer == expected_answer, f"Ошибка. Ожидали: {expected_answer}, а получили: {actual_answer}"
    def test_get_answer_to_question_4(self, driver):
        with allure.step('Проверка ответа на вопрос 4'):
            faq_page = FAQPage(driver)
            faq_page.open_page()
            faq_page.check_faq_section_title()
            faq_page.scroll_to_faq_section()
            faq_page.click_question(FAQLocators.QUESTION_4)
            actual_answer = faq_page.get_answer_text(FAQLocators.ANSWER_4)
            expected_answer = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
            assert actual_answer == expected_answer, f"Ошибка. Ожидали: {expected_answer}, а получили: {actual_answer}"
    def test_get_answer_to_question_5(self, driver):
        with allure.step('Проверка ответа на вопрос 5'):
            faq_page = FAQPage(driver)
            faq_page.open_page()
            faq_page.check_faq_section_title()
            faq_page.scroll_to_faq_section()
            faq_page.click_question(FAQLocators.QUESTION_5)
            actual_answer = faq_page.get_answer_text(FAQLocators.ANSWER_5)
            expected_answer = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
            assert actual_answer == expected_answer, f"Ошибка. Ожидали: {expected_answer}, а получили: {actual_answer}"
    def test_get_answer_to_question_6(self, driver):
        with allure.step('Проверка ответа на вопрос 6'):
            faq_page = FAQPage(driver)
            faq_page.open_page()
            faq_page.check_faq_section_title()
            faq_page.scroll_to_faq_section()
            faq_page.click_question(FAQLocators.QUESTION_6)
            actual_answer = faq_page.get_answer_text(FAQLocators.ANSWER_6)
            expected_answer = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
            assert actual_answer == expected_answer, f"Ошибка. Ожидали: {expected_answer}, а получили: {actual_answer}"
    def test_get_answer_to_question_7(self, driver):
        with allure.step('Проверка ответа на вопрос 7'):
            faq_page = FAQPage(driver)
            faq_page.open_page()
            faq_page.check_faq_section_title()
            faq_page.scroll_to_faq_section()
            faq_page.click_question(FAQLocators.QUESTION_7)
            actual_answer = faq_page.get_answer_text(FAQLocators.ANSWER_7)
            expected_answer = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
            assert actual_answer == expected_answer, f"Ошибка. Ожидали: {expected_answer}, а получили: {actual_answer}"
    def test_get_answer_to_question_8(self, driver):
        with allure.step('Проверка ответа на вопрос 8'):
            faq_page = FAQPage(driver)
            faq_page.open_page()
            faq_page.check_faq_section_title()
            faq_page.scroll_to_faq_section()
            faq_page.click_question(FAQLocators.QUESTION_8)
            actual_answer = faq_page.get_answer_text(FAQLocators.ANSWER_8)
            expected_answer = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
            assert actual_answer == expected_answer, f"Ошибка. Ожидали: {expected_answer}, а получили: {actual_answer}"
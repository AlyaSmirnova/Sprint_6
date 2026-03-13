from pages.faq_page import FAQPage
from src.locators import FAQLocators
import allure
import pytest


@allure.suite('Main Page Tests')
@allure.feature('FAQ Section: "Important Questions"')
class TestFaqPage:
    FAQ_TEST_DATA = [
        (FAQLocators.QUESTION_1, FAQLocators.ANSWER_1, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (FAQLocators.QUESTION_2, FAQLocators.ANSWER_2, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (FAQLocators.QUESTION_3, FAQLocators.ANSWER_3, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (FAQLocators.QUESTION_4, FAQLocators.ANSWER_4, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (FAQLocators.QUESTION_5, FAQLocators.ANSWER_5, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (FAQLocators.QUESTION_6, FAQLocators.ANSWER_6, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (FAQLocators.QUESTION_7, FAQLocators.ANSWER_7, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (FAQLocators.QUESTION_8, FAQLocators.ANSWER_8, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ]

    @allure.title('Check FAQ answer for: {expected_answer}')
    @allure.description('Verify that clicking on a question reveals the correct answer text')
    @pytest.mark.parametrize('question_locator, answer_locator, expected_answer', FAQ_TEST_DATA)
    def test_get_answer_to_question(self, driver, question_locator, answer_locator, expected_answer):
        faq_page = FAQPage(driver)
        with allure.step('Open FAQ page'):
            faq_page.open_page()
        with allure.step('Scroll to FAQ section'):
            faq_page.check_faq_section_title()
            faq_page.scroll_to_faq_section()
        with allure.step('Click on the question and retrieve the answer'):
            faq_page.click_question(question_locator)
            actual_answer = faq_page.get_answer_text(answer_locator)
        with allure.step('Verify the answer text'):
            assert actual_answer == expected_answer, f'Assertion failed! Expected: {expected_answer}, but got: {actual_answer}'

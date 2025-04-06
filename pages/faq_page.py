from pages.base_page import BasePage
from src.locators import FAQLocators
import allure


class FAQPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        with allure.step('Открыть страницу'):
            self.navigate()

    def check_faq_section_title(self):
        with allure.step('Дождаться появления заголовка секции "Вопросы о важном"'):
            return self.wait_for_element(FAQLocators.FAQ_SECTION_TITLE)

    def scroll_to_faq_section(self):
        with allure.step('Проскроллить страницу до секции "Вопросы о важном"'):
            self.scroll_to_element(FAQLocators.FAQ_SECTION_TITLE)

    def click_question(self, question_locator):
        with allure.step('Кликнуть на иконку для раскрытия вопроса'):
            self.click_element(question_locator)

    def get_answer_text(self, answer_locator):
        with allure.step('Получить текст ответа на вопрос'):
            return self.get_element_text(answer_locator)
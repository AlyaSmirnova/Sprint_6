from pages.base_page import BasePage
from src.locators import FAQLocators
import allure


class FAQPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Open the FAQ page')
    def open_page(self):
        self.navigate()

    @allure.step('Wait for the "FAQ" section title to appear')
    def check_faq_section_title(self):
        return self.wait_for_element(FAQLocators.FAQ_SECTION_TITLE)

    @allure.step('Scroll down to the "Important Questions" section')
    def scroll_to_faq_section(self):
        self.scroll_to_element(FAQLocators.FAQ_SECTION_TITLE)

    @allure.step('Expand the question: {question_locator}')
    def click_question(self, question_locator):
        element = self.wait_for_element(question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Retrieve the answer text: {answer_locator}')
    def get_answer_text(self, answer_locator):
        return self.get_element_text(answer_locator)

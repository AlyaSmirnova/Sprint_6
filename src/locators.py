from selenium.webdriver.common.by import By


class FAQLocators:
    FAQ_SECTION_TITLE = By.XPATH, "//div[text()='Вопросы о важном']"
    QUESTION_1 = By.ID, "accordion__heading-0"
    QUESTION_2 = By.ID, "accordion__heading-1"
    QUESTION_3 = By.ID, "accordion__heading-2"
    QUESTION_4 = By.ID, "accordion__heading-3"
    QUESTION_5 = By.ID, "accordion__heading-4"
    QUESTION_6 = By.ID, "accordion__heading-5"
    QUESTION_7 = By.ID, "accordion__heading-6"
    QUESTION_8 = By.ID, "accordion__heading-7"

    ANSWER_1 = By.ID, "accordion__panel-0"
    ANSWER_2 = By.ID, "accordion__panel-1"
    ANSWER_3 = By.ID, "accordion__panel-2"
    ANSWER_4 = By.ID, "accordion__panel-3"
    ANSWER_5 = By.ID, "accordion__panel-4"
    ANSWER_6 = By.ID, "accordion__panel-5"
    ANSWER_7 = By.ID, "accordion__panel-6"
    ANSWER_8 = By.ID, "accordion__panel-7"

class MainPageLocators:
    ORDER_BUTTON_TOP = By.XPATH, "//button[contains(text() = 'Заказать') and @class = 'Button_Button__ra12g']"
    ORDER_BUTTON_BOTTOM = By.XPATH, "//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать')]"
    SCOOTER_LOGO = By.CLASS_NAME, "//Header_LogoScooter__31sAR"
    YANDEX_LOGO = By.CLASS_NAME, "//Header_LogoYandex__3TSOI"

class OrderPageLocators:
    ORDER_HEADER = By.XPATH, "//div[contains(text()='Для кого самокат')]"
    FIRST_NAME = By.XPATH, "//input[@placeholder = '* Имя']"
    LAST_NAME = By.XPATH, "//input[@placeholder = '* Фамилия']"
    ADDRESS = By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']"
    METRO_STATION = By.XPATH, "//input[@placeholder = '* Станция метро']"
    METRO_OPTION = By.XPATH, "//div[text() = '{}']"
    PHONE = By.XPATH, "//input[@olaceholder = '* Телефон: на него позвонит курьер']"
    BUTTON_NEXT = By.XPATH, "//button[text() = 'Далее']"

    DATE = By.XPATH, "input[@placeholder = '* Когда привезти самокат']"
    RENTAL_TIME = By.CLASS_NAME, "Dropdown-placeholder"
    RENTAL_OPTION = By.XPATH, "//div[text() = '{}']"
    COLOR = By.ID, "{}"
    COMMENT = By.XPATH, "//input[@placeholder = 'Комментарий для курьера']"
    ORDER_BUTTON = By.XPATH, "//button[contains(@class, 'Button_Middle') and text() = 'Заказать']"
    CONFIRMATION_BUTTON = By.XPATH, "//button[text() = 'Да']"
    SUCCESS_MESSAGE = By.XPATH, "//dix[contains(@class, 'Order_ModalHeader')]"
from selenium.webdriver.common.by import By

class MainPageLocators:

    QUESTION_LOCATOR = By.XPATH, '//*[@class="my-question-locator-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//*[@class="my-answer-locator-{}"]'
    QUESTION_LOCATOR_TO_SCROLL = By.XPATH, '//*[@class="my-question-locator-7"]'
    ORDER_BUTTON_UP = By.XPATH, '//button[@class="Button_Button__ra12g"]'
    ORDER_BUTTON_DOWN = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
    LOGO_LOCATOR = By.XPATH, '//img[@alt="Scooter"]'
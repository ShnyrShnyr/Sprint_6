from selenium.webdriver.common.by import By

class MainPageLocators:

    QUESTION_LOCATOR = By.XPATH, '//div[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//div[@aria-labelledby="accordion__heading-{}"]'
    QUESTION_LOCATOR_TO_SCROLL = By.XPATH,'//div[@id="accordion__heading-7"]'
    ORDER_BUTTON_UP = By.XPATH, '//button[@class="Button_Button__ra12g"]'
    ORDER_BUTTON_DOWN = By.CLASS_NAME, 'Button_Middle__1CSJM'
    CHECK_MAIN_PAGE = By.CLASS_NAME, 'Home_FirstPart__3g6vG'
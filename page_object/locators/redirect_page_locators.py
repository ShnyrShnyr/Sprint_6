from selenium.webdriver.common.by import By

class RedirectPageLocators:
    LOGO_SCOOTER = By.XPATH, '//*[@alt="Scooter"]'
    LOGO_YANDEX = By.XPATH, '//*[@alt="Yandex"]'
    MAIN_ELEMENT_ON_SCOOTER_PAGE = By.CLASS_NAME, 'Home_FirstPart__3g6vG'
    FIND_BUTTON_ON_YANDEX_PAGE = By.XPATH, '//*[text()="Скачайте приложение Дзена"]'

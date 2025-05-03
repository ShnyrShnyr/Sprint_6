from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_FIELD = By.XPATH, '//input[@placeholder="* Имя"]'
    SURNAME_FIELD = By.XPATH, '//input[@placeholder="* Фамилия"]'
    ADRESS_FIELD = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    METRO_STATION = By.XPATH, '//input[@placeholder="* Станция метро"]'
    PHONE_FIELD = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    NEXT_BUTTON = By.XPATH, '//button[text()="Далее"]'
    PRO_ARENDY_HEADER = By.XPATH, '//div[@class="Order_Header__BZXOb"]'
    START_RENT_FIELD = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    RENT_DAYS_DROPDOWN = By.XPATH, '//div[@class="Dropdown-placeholder"]'
    BLACK_CHECKBOX = By.XPATH, '//input[@id="black"]'
    GREY_CHECKBOX = By.XPATH, '//input[@id="grey"]'
    COMMENT_FIELD = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    ORDER_BUTTON = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]'
    PRE_CONFIRM_ORDER = By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]'
    YES_BUTTON = By.XPATH, '//div[text()="Да"]'
    CONFIRM_ORDER = By.XPATH, '//div[text()="Заказ оформлен"]'



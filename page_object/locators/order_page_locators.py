from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_FIELD = By.XPATH, '//input[@placeholder="* Имя"]'
    SURNAME_FIELD = By.XPATH, '//input[@placeholder="* Фамилия"]'
    ADDRESS_FIELD = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    METRO_FIELD = By.XPATH, '//input[@placeholder="* Станция метро"]'
    METRO_DROPDOWN_SOKOLNIKI = By.XPATH, "//button[contains(@class, 'Order_SelectOption__82bhS') and @value=4]"
    PHONE_FIELD = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    NEXT_BUTTON = By.XPATH, '//button[text()="Далее"]'
    START_RENT_FIELD = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    RENT_DAYS_FIELD = By.XPATH, '//div[@class="Dropdown-placeholder"]'
    TWO_DAYS_DROPDOWN = By.XPATH, '//*[text()="двое суток" and @aria-selected="false"]'
    BLACK_CHECKBOX = By.XPATH, '//input[@id="black"]'
    GREY_CHECKBOX = By.XPATH, '//input[@id="grey"]'
    COMMENT_FIELD = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    ORDER_BUTTON = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]'
    PRE_CONFIRM_ORDER = By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]'
    YES_BUTTON = By.XPATH, '//*[text()="Да"]'
    CONFIRM_ORDER = By.XPATH, '//*[text()="Заказ оформлен"]'
    ACCEPT_COOKIE_BUTTON = By.ID, 'rcc-confirm-button'


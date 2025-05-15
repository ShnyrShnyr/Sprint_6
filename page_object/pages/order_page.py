from page_object.pages.base_page import BasePage
from page_object.locators.order_page_locators import OrderPageLocators
import allure
from datetime import datetime, timedelta

class OrderPage(BasePage):

    @allure.step('Создаем заказ')
    def set_order(self, data, flag):
        self.add_text_to_element(OrderPageLocators.NAME_FIELD, data['name'])
        self.add_text_to_element(OrderPageLocators.SURNAME_FIELD, data['surname'])
        self.add_text_to_element(OrderPageLocators.ADDRESS_FIELD, data['address'])
        self.click_to_element(OrderPageLocators.METRO_FIELD)
        self.click_to_element(OrderPageLocators.METRO_DROPDOWN_SOKOLNIKI)
        self.add_text_to_element(OrderPageLocators.PHONE_FIELD, data['phone'])
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)
        self.create_tomorrow_date()
        self.click_to_element(OrderPageLocators.RENT_DAYS_FIELD)
        self.click_to_element(OrderPageLocators.TWO_DAYS_DROPDOWN)
        self.click_to_element(flag)
        self.add_text_to_element(OrderPageLocators.COMMENT_FIELD, data['comment'])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.YES_BUTTON)
        self.click_to_element(OrderPageLocators.ACCEPT_COOKIE_BUTTON)

    @allure.step('Проверяем заказ')
    def check_order(self, locator):
        return self.get_text_from_element(locator)

    @allure.step('Выбираем дату следующий день')
    def create_tomorrow_date(self):
        self.click_to_element(OrderPageLocators.START_RENT_FIELD)
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_str = tomorrow.strftime('%d.%m.%y')
        self.add_text_to_element_with_enter(OrderPageLocators.START_RENT_FIELD, tomorrow_str)

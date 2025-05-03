from page_object.pages.base_page import BasePage
from page_object.locators.order_page_locators import OrderPageLocators
from page_object.data import Data


class OrderPage(BasePage):

    def set_order(self, data):
        self.click_to_element(data['station_locator'])
        self.add_text_to_element(OrderPageLocators.NAME_FIELD, data['name'])
        self.add_text_to_element(OrderPageLocators.SURNAME_FIELD, data['surname'])
        self.add_text_to_element(OrderPageLocators.ADRESS_FIELD, data['adress'])
        self.click_to_element(time)
        self.click_to_element(button_locator)

    def check_order(self, locator):
        return self.get_text_from_element(locator)

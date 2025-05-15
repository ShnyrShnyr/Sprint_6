import pytest
import allure

from page_object.locators.main_page_locators import MainPageLocators
from page_object.locators.order_page_locators import OrderPageLocators
from page_object.pages.main_page import MainPage
from page_object.pages.order_page import OrderPage
from page_object.data import Data

test1 = [MainPageLocators.ORDER_BUTTON_UP, Data.ORDER_DATA_1, OrderPageLocators.BLACK_CHECKBOX]
test2 = [MainPageLocators.ORDER_BUTTON_DOWN, Data.ORDER_DATA_2, OrderPageLocators.GREY_CHECKBOX]

class TestOrderPage:

    @pytest.mark.parametrize(
        'locator, order_data, flag',
        [
            test1,
            test2
        ]
    )
    @allure.title('Тест на создание заказа')
    def test_create_order(self, driver, locator, order_data, flag):
        main_page = MainPage(driver)
        main_page.go_to_url(Data.URL_MAIN_PAGE)
        main_page.scroll_to_element(locator)
        main_page.click_to_element(locator)
        order_page = OrderPage(driver)
        order_page.set_order(order_data, flag)
        assert Data.CONFIRM_TEXT in order_page.check_order()

import allure
import pytest

from conftest import main_page
from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.main_page import MainPage
from page_object.pages.order_page import OrderPage
from page_object.data import Data

@allure.title('Тесты на проверку вопросов')
class TestMainPage:

    @pytest.mark.parametrize(
        'num',
        [0,
         1,
         2,
         3,
         4,
         5,
         6,
         7]
    )
    def test_question_and_answer(self, main_page, num):
        main_page.click_to_question(num)
        assert main_page.get_answer_text(num) == Data.ANSWER_DATA(num)

    @pytest.mark.parametrize(
        'locator, order_data',
        [
            (MainPageLocators.ORDER_BUTTON_UP, Data.ORDER_DATA_1),
            (MainPageLocators.ORDER_BUTTON_DOWN, Data.ORDER_DATA_2)
        ]
    )
    def test_create_order(self, driver, locator, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_to_element(locator)
        order_page.set_order(order_data)
        assert order_page.check_order

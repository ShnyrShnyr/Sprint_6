import allure
import pytest

from conftest import main_page
from page_object.data import Data


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
    @allure.title('Тест на проверку вопросов')
    def test_question_and_answer(self, main_page, num):
        main_page.click_to_question(num)
        assert main_page.get_answer_text(num) == Data.ANSWER_DATA[num]

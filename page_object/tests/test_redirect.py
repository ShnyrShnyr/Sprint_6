import allure
from page_object.data import Data
from page_object.pages.redirect_page import RedirectPage


class TestRedirect:

    @allure.title('Тест на проверку перехода Самокат')
    def test_redirect_scooter(self, driver):
        redirect_page = RedirectPage(driver)
        redirect_page.go_to_url(Data.URL_ORDER_PAGE)
        element = redirect_page.click_to_logo_scooter()
        assert element.is_displayed()

    @allure.title('Тест на проверку перехода Яндекс')
    def test_redirect_yandex(self,driver):
        redirect_page = RedirectPage(driver)
        redirect_page.go_to_url(Data.URL_ORDER_PAGE)
        element = redirect_page.click_to_logo_yandex()
        assert element.is_displayed()

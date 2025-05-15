import allure
from page_object.locators.redirect_page_locators import RedirectPageLocators
from page_object.pages.base_page import BasePage

class RedirectPage(BasePage):

    @allure.step('Проверяем переход по лого Самокат')
    def click_to_logo_scooter(self):
        self.click_to_element(RedirectPageLocators.LOGO_SCOOTER)
        return self.find_element_with_wait(RedirectPageLocators.MAIN_ELEMENT_ON_SCOOTER_PAGE)

    @allure.step('Проверяем переход по лого Яндекс')
    def click_to_logo_yandex(self):
        self.click_to_element(RedirectPageLocators.LOGO_YANDEX)
        self.switch_to_window()
        return self.find_element_with_wait(RedirectPageLocators.FIND_BUTTON_ON_YANDEX_PAGE)

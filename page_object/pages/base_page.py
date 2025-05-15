from selenium.webdriver.support.wait import WebDriverWait
from page_object.data import Data
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, Data.TIMEOUT).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def go_to_url(self, url):
        self.driver.get(url)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, Data.TIMEOUT).until(ec.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def add_text_to_element_with_enter(self,locator, text):
        self.find_element_with_wait(locator).send_keys(text + Keys.ENTER)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @staticmethod
    def format_locators(locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    def switch_to_window(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])
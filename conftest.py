import pytest
from selenium import webdriver
from page_object.pages.main_page import MainPage
from page_object.data import Data


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.go_to_url(Data.URL_MAIN_PAGE)
    return page

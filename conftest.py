import pytest
from selenium import webdriver
from pages.main_page import MainPage



@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(15)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def open_main_page(driver):
    return MainPage(driver)


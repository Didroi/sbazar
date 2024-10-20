import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.praha_page import PrahaPage
from time import sleep



@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(15)
    driver.maximize_window()
    yield driver
    sleep(3)  #its just for tests if i'll forget delete it
    driver.quit()

@pytest.fixture()
def open_main_page(driver):
    return MainPage(driver)

@pytest.fixture()
def prague_page(driver):
    return PrahaPage(driver)

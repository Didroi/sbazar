import pytest
from selenium import webdriver
from test_ui_dmitrii.pages.create_new_customer_account import NewCustomerAccount



@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(15)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def create_account_page(driver):
    return NewCustomerAccount(driver)


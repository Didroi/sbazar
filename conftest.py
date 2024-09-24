import pytest
from selenium import webdriver
from test_ui_dmitrii.pages.create_new_customer_account import NewCustomerAccount
from test_ui_dmitrii.pages.eco_friendly_supplies import EcoProducts
from test_ui_dmitrii.pages.my_account import MyAccountPage
from test_ui_dmitrii.pages.product_page import ProductPage
from test_ui_dmitrii.pages.login_page import LoginPage
from test_ui_dmitrii.pages.sales_page import Sales
from test_ui_dmitrii.pages.deals_page import DealsPage


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


@pytest.fixture()
def eco_products_page(driver):
    return EcoProducts(driver)


@pytest.fixture()
def my_account_page(driver):
    return MyAccountPage(driver)


@pytest.fixture()
def product_page(driver):
    return ProductPage(driver)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def sales_page(driver):
    return Sales(driver)


@pytest.fixture()
def deals_page(driver):
    return DealsPage(driver)

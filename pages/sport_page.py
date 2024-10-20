import allure
from pages.base_page import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class SportPage(BasePage):
    title_text = 'Sport'
    title_class_name = 'c-bread-crumbs__header'

    @allure.step('Going to target page')
    def open_sport_supplies_page(self):
        self.open()
        self.changing_page((By.XPATH, '//*[@class="c-categories__name" and contains(text(), "Sport")]'))

    @allure.step('Check title')
    def is_title_correct(self):
        return self.is_text_present(self.title_text, self.title_class_name)

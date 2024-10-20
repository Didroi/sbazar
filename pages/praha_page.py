import allure
from pages.base_page import BasePage
from pages.main_page import MainPage
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class PrahaPage(BasePage):
    # page_url = '0-vsechny-kategorie/praha'
    @allure.step('Going to target page')
    def open_prague_page(self):
        self.open()
        self.changing_page('[aria-controls="react-autowhatever-1"]', 'react-autowhatever-1-section-1-item-0')

    @allure.step('Check localized place')
    def is_localized_text_present(self):
        return self.is_text_present('Praha', 'p-uw-item-list__items-count__locality')

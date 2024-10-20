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
        self.changing_page(
            (By.CSS_SELECTOR, '[aria-controls="react-autowhatever-1"]'),
            (By.ID, 'react-autowhatever-1-section-1-item-0')
        )

    @allure.step('Check localized place')
    def is_localized_text_present(self):
        return self.is_text_present('Praha', 'p-uw-item-list__items-count__locality')

    @allure.step('Go to main page by clicking logo')
    def click_to_logo_to_switch_to_main(self):
        self.click((By.CLASS_NAME, 'ribbon-service__logo'))

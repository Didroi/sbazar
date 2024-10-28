import allure
from pages.base_page import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class SignInModalWindow(BasePage):

    def open_help(self):
        self.switch_to_new_window()
        self.click((By.CSS_SELECTOR, '[data-locale="footer.help"]'))

    def check_correct_page_is_open(self):
        actual_tabs = self.driver.window_handles
        self.driver.switch_to.window(actual_tabs[1])
        return self.check_url_contains('prihlaseni-seznam-ucet')


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

    def click_to_login_input(self):
        self.click((By.ID, 'login-username'))

    def click_create_new_account(self):
        self.switch_to_new_window()
        self.wait()
        self.click_to_login_input()
        self.click((By.CSS_SELECTOR, '[data-locale="login.register.link"]'))

    def choose_email_creation_link(self):
        self.wait()
        self.click((By.CSS_SELECTOR, '[data-locale="register.intro.own.title"]'))

    def enter_email(self):
        input = self.find((By.ID, 'register-username'))
        input.send_keys('ddd@ddd.ru')
        self.wait()
        self.click((By.XPATH, 'button[@type="submit"]'))

    def fill_account_creating_form(self):
        pass


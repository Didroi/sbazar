import allure
from selenium.webdriver.common.by import By
from test_ui_dmitrii.pages.base_page import BasePage
import string
import secrets


class NewCustomerAccount(BasePage):
    page_url = 'customer/account/create/'

    def generate_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password

    # @allure.step('Password Generation')
    def fill_password_input(self, locate_id, length=12):
        self.password = self.generate_password(length)
        # print(self.password)
        self.fill_input_by_id(locate_id, self.password)
        return self.password

    def fill_password_confirmation(self, locate_id, confirmation_password=None):
        if not confirmation_password:
            confirmation_password = self.password
        # print(confirmation_password)
        self.fill_input_by_id(locate_id, confirmation_password)

    @allure.step('Check incorrect password to confirm')
    def check_incorrect_password_to_confirm(self):
        return self.find((By.ID, 'password-confirmation-error')).is_displayed()

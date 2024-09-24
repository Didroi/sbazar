from test_ui_dmitrii.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def check_unverified_action_opened(self, locator):
        return 'You must login or register to add items to your wishlist' in self.find(locator).text

from test_ui_dmitrii.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DealsPage(BasePage):

    def check_opened_correct_page(self, text):
        return text in self.find((By.XPATH, '//span[@data-ui-id="page-title-wrapper"]')).text

import allure
from selenium.webdriver.common.by import By
from test_ui_dmitrii.pages.base_page import BasePage


class Sales(BasePage):
    page_url = 'sale.html'
    h1_text = 'Sale'

    @allure.step('Check sales page opened')
    def check_sale_page_opened(self):
        return self.check_correct_page_opened(self.h1_text)

    @allure.step('Move to Some Deal Page')
    def go_to_deal_page(self, text):
        self.find((By.XPATH, f'//strong[contains(text(), "{text}")]')).click()

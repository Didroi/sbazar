from test_ui_dmitrii.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MyAccountPage(BasePage):
    page_url = '/customer/account/'

    def check_correct_account_information(self, *my_tuple):
        reg_information = self.find((By.XPATH, '//div[@class="box-content"]/p'))
        for el in my_tuple:
            # print(el)
            yield el in reg_information.text

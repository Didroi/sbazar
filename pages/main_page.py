import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    page_title = 'Bazar a inzerce zdarma - Sbazar.cz'

    @allure.step('Check Title')
    def is_text_present(self):
        return 'Vyberte si z' in self.find((By.CLASS_NAME, 'p-uw-item-list__items-count')).text

    @allure.step('Changing region')
    def changing_region(self):
        self.find((By.ID, 'filter-locality-suggest')).click()
        self.click((By.XPATH, '//div[@class = "react-autosuggest__section-container"]/span[contains(text(), "Praha")]'))

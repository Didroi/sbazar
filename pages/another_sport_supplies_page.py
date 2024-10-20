import allure
from pages.sport_page import SportPage
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class AnotherSportSuppliesPage(SportPage):
    title_text = 'Ostatní sportovní vybavení'

    @allure.step('Going to target page')
    def open_another_sport_supplies_page(self):
        self.open_sport_supplies_page()
        self.click((By.XPATH, '//a[@class="c-categories__name" and contains(text(), "Ostatní sportovní vybavení")]'))


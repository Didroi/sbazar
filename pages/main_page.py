import allure
from pages.base_page import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class MainPage(BasePage):
    page_title = 'Bazar a inzerce zdarma - Sbazar.cz'
    sort_by = None
    sort_order = None


    @allure.step('Changing region')
    def changing_region(self):
        self.changing_page('[aria-controls="react-autowhatever-1"]', 'react-autowhatever-1-section-1-item-0')

    @allure.step('Sorting products')
    def sorting_by_(self, sort_by = 'price', sort_order = 'asc'):
        self.wait()
        self.click((By.ID, 'filter-sort-opener'))
        # self.wait()
        if sort_by == 'age':
            self.click((By.XPATH, '//a[@data-dot="od-nejnovejsich"]'))
        elif sort_by == 'price':
            if sort_order == 'desc':
                self.click((By.XPATH, '//a[@data-dot="od-nejdrazsich"]'))
            else:
                self.click((By.XPATH, '//a[@data-dot="od-nejlevnejsich"]'))
        else:
            print("'sort_by' can be only 'age' or 'price'")
        self.sort_by = sort_by
        self.sort_order = sort_order

    def is_sorting_correct(self):
        returned_text = None
        if self.sort_by == 'age':
            returned_text = 'Nejnovější nabídky'
        elif self.sort_by == 'price':
            if self.sort_order == 'desc':
                returned_text = 'Nejdražší nabídky'
            else:
                returned_text = 'Nejlevnější nabídky'
        else:
            print("Need to define a method 'sorting_by_'")
        return self.find((By.CLASS_NAME, 'p-uw-item-list__page-title')).text == returned_text

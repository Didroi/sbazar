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
        self.changing_page(
            (By.CSS_SELECTOR, '[aria-controls="react-autowhatever-1"]'),
            (By.ID, 'react-autowhatever-1-section-1-item-0')
        )

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

    @allure.step('Click to Login link')
    def click_to_login_lnk(self):
        shadow_root = self.find((By.XPATH, '//szn-login-widget[@data-dot="login-badge"]')).shadow_root

        # shadow_root = self.driver.find_element(By.XPATH, '//szn-login-widget[@data-dot="login-badge"]').shadow_root # это элемент перед shadow DOM
        login_link = shadow_root.find_element(By.ID, 'login')
        # print(login_link.text)
        # login_link.click()

        # shadow_host = WebDriverWait(self.driver, 10).until(
        #     ec.presence_of_element_located((By.CSS_SELECTOR, "szn-login-widget"))
        # )
        # shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host)
        # login_link = shadow_root.find_element(By.CSS_SELECTOR, "#login")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", login_link)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(login_link))
        login_link.click()

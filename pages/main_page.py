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

    # @allure.step('Check Title')
    # def is_text_present(self, text = 'Vyberte si z', class_name = 'p-uw-item-list__items-count'):
    #     return text in self.find((By.CLASS_NAME, class_name)).text

    # @allure.step('Check localized place')
    # def is_localized_text_present(self):
    #     return self.is_text_present('Praha', 'p-uw-item-list__items-count__locality')

    @allure.step('Changing region')
    def changing_region(self):
        # sleep(2)
        # try:
        #     WebDriverWait(self.driver, 1).until(lambda driver: driver.find_element(By.ID, ' '))
        # except (TimeoutException, NoSuchElementException):
        #     pass

        self.wait()

        region_input = self.find((By.CSS_SELECTOR, '[aria-controls="react-autowhatever-1"]'))
        region_input.click()
        self.click((By.ID, 'react-autowhatever-1-section-1-item-0'))

        # WebDriverWait(self.driver, 30).until(
        #     lambda driver: driver.execute_script("return document.readyState") == "complete"
        # )
        # max_attempts, attempts = 4, 0
        #
        # while attempts < max_attempts:
        #     try:
        #         region_input = WebDriverWait(self.driver, 30).until(
        #             ec.element_to_be_clickable((By.CSS_SELECTOR, '[aria-controls="react-autowhatever-1"]'))
        #         )
        #         region_input.click()
        #
        #         dropdown_item = WebDriverWait(self.driver, 30).until(
        #             ec.element_to_be_clickable((By.ID, 'react-autowhatever-1-section-1-item-0'))
        #         )
        #         dropdown_item.click()
        #         break
        #     except StaleElementReferenceException:
        #         attempts += 1
        #         if attempts == max_attempts:
        #             raise

    @allure.step('Sorting products')
    def sorting_by_(self, sort_by = 'price', sort_order = 'asc'):
        # path = '//a[@class="c-filter-sort__link"'
        self.wait()
        self.click((By.ID, 'filter-sort-opener'))
        # self.wait()
        if sort_by == 'age':
            # WebDriverWait(self.driver, 10).until(
            #             ec.element_to_be_selected(By.XPATH, '//a[@data-dot="od-nejnovejsich"]')
            #         )
            self.click((By.XPATH, '//a[@data-dot="od-nejnovejsich"]'))
        elif sort_by == 'price':
            if sort_order == 'desc':
                self.click((By.XPATH, '//a[@data-dot="od-nejdrazsich"]'))
            else:
                # self.wait()
                self.click((By.XPATH, '//a[@data-dot="od-nejlevnejsich"]'))
        else:
            print("'sort_by' can be only 'age' or 'price'")
        self.sort_by = sort_by
        self.sort_order = sort_order

    def is_sorting_correct(self):
        returned_text = None
        # print('VAR')
        # print(self.sort_by)
        # print(self.sort_order)
        if self.sort_by == 'age':
            returned_text = 'Nejnovější nabídky'
        elif self.sort_by == 'price':
            if self.sort_order == 'desc':
                returned_text = 'Nejdražší nabídky'
            else:
                returned_text = 'Nejlevnější nabídky'
        else:
            print("Need to define a method 'sorting_by_'")
        # print(returned_text)
        # print(self.sort_by)
        # print(self.sort_order)
        # print(self.find((By.CLASS_NAME, 'p-uw-item-list__page-title')).text)
        return self.find((By.CLASS_NAME, 'p-uw-item-list__page-title')).text == returned_text

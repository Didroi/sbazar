import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    base_url = 'https://www.sbazar.cz/'
    page_url = None
    page_title = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Open page')
    def open(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            self.driver.get(self.base_url)

    @allure.step('Check Title')
    def is_title_correct(self):
        return self.driver.title == self.page_title

    @allure.step('Scroll the page')
    def scroll_page(self, pixels=None, start=0):
        if pixels:
            self.driver.execute_script(f"window.scrollTo({start}, {pixels})")
        else:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def find(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(ec.presence_of_element_located(locator))

    def click(self, locator):
        self.find(locator).click()


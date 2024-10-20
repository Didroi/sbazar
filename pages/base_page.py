import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchFrameException


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
        # self.wait(2)


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

    def wait(self, time=0.1):
        try:
            WebDriverWait(self.driver, time).until(lambda driver: driver.find_element(By.ID, ' '))
        # except (TimeoutException, NoSuchElementException):
        except (TimeoutException, NoSuchElementException, NoSuchFrameException):
            pass

    @allure.step('Check Title')
    def is_text_present(self, text='Vyberte si z', class_name='p-uw-item-list__items-count'):
        return text in self.find((By.CLASS_NAME, class_name)).text

    def changing_page(self, locator, locator_2 = None):

        self.wait()

        changing_page = self.find((By.CSS_SELECTOR, locator))
        changing_page.click()
        if locator_2:
            self.click((By.ID, locator_2))

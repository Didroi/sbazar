import allure
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    base_url = 'https://www.sbazar.cz//'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Open page')
    def open(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Unable to open that page by url')
        print(self.driver.title)


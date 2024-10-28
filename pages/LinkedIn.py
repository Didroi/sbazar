import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchFrameException
from time import sleep


class LinkedIn:
    base_url = 'https://www.linkedin.com/'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_linkedin(self):
        self.driver.get(self.base_url)

    def push_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test-id="home-hero-sign-in-cta"]')
        sleep(2)
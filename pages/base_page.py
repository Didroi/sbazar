import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Open page')
    def open(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Unable to open that page by url')

    @allure.step('Scroll the page')
    def scroll_page(self, pixels=None, start=0):
        if pixels:
            self.driver.execute_script(f"window.scrollTo({start}, {pixels})")
        else:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def find(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(
            ec.presence_of_element_located(locator)
        )

    @allure.step('Fill Input by ID')
    def fill_input_by_id(self, locate_id, input_text):
        self.find((By.ID, locate_id)).send_keys(input_text)

    @allure.step('Push the button')
    def push_the_button(self, button_selector):
        # self.find((By.XPATH, f'//button[@{button_selector}]')).click()
        locator = (By.XPATH, f'//button[@{button_selector}]')
        button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))
        button.click()

    @allure.step('Required field check')
    def check_required_field(self):
        return self.find((By.XPATH, '//div[contains(text(),"This is a required field.")]')).is_displayed()

    @allure.step('Move attention')
    def move_attention(self, driver, locator):
        target = self.find(locator)
        ActionChains(driver).move_to_element(target).perform()

    def check_correct_page_opened(self, text):
        return text in self.find((By.XPATH, f'//h1[@id="page-title-heading"]/span[contains(text(), {text})]')).text

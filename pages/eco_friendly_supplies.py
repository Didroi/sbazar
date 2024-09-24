import allure
from selenium.webdriver.common.by import By
from test_ui_dmitrii.pages.base_page import BasePage


class EcoProducts(BasePage):
    page_url = 'collections/eco-friendly.html'

    @allure.step('Choose Eco product')
    def choose_eco_product(self, locator_text):
        product_page = self.find((By.XPATH, f'//a[contains(text(), "{locator_text}")]'))
        url_link = product_page.get_attribute('href')
        self.eco_product_page_url = url_link[url_link.find('.com/') + 5:]
        product_page.click()

    @allure.step('Add to favorite')
    def click_to_favorite(self, locator):
        # print(locator)
        self.find(locator).click()

    @allure.step('Sorting by parameter')
    def sorting_by_(self, locator_1, locator_2):
        self.find(('xpath', locator_1)).click()
        self.find(('xpath', locator_2)).click()

    @allure.step('Check cheapest product is first')
    def check_order_by_price(self, locator):
        '''
        В реальном проекте нужно использовать реальную фильтрацию по цене.
        Я бы взял список цен из БД, или из апи-метода, возвращаюшего список всех товаров и отсортировал.
        Но здесь нет ни того ни другого, к сожалению.
        Как вараинт еще можно собрать весь список товаров Селениумом и осортировать. Но мне лениво так делать.
        Я же просто хардкожу минимальную цену.
        Я осознаю, что на реальном пректе так делать нельзя!
        '''
        return '$18' in self.find(('xpath', locator)).text

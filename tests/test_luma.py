import random as r
import string as s


default_name = 'Dmitrii'
default_surname = 'Kiselev'
default_email = f'{"".join(r.choices(s.ascii_lowercase, k=5))}@yandex.ru'
name = 'ria Bikram Pant'


def test_new_customer_account_creation(create_account_page, my_account_page):
    create_account_page.open()
    create_account_page.fill_input_by_id('firstname', default_name)
    create_account_page.fill_input_by_id('lastname', default_surname)
    create_account_page.fill_input_by_id('email_address', default_email)
    create_account_page.fill_password_input('password')
    create_account_page.fill_password_confirmation('password-confirmation')
    create_account_page.scroll_page()
    create_account_page.push_the_button('title="Create an Account"')
    assert my_account_page.check_correct_account_information(default_name, default_surname, default_email)


def test_without_name(create_account_page):
    create_account_page.open()
    create_account_page.fill_input_by_id('lastname', default_surname)
    create_account_page.fill_input_by_id('email_address', default_email)
    create_account_page.fill_password_input('password')
    create_account_page.fill_password_confirmation('password-confirmation')
    create_account_page.scroll_page()
    create_account_page.push_the_button('title="Create an Account"')
    assert create_account_page.check_required_field()


def test_incorrect_password_confirmation(create_account_page):
    create_account_page.open()
    create_account_page.fill_input_by_id('lastname', default_surname)
    create_account_page.fill_input_by_id('email_address', default_email)
    create_account_page.fill_password_input('password')
    create_account_page.fill_password_confirmation('password-confirmation', '11')
    create_account_page.scroll_page()
    create_account_page.push_the_button('title="Create an Account"')
    assert create_account_page.check_incorrect_password_to_confirm()


def test_opening_eco_product_page(eco_products_page, product_page):
    locator = ('xpath', '//span[@itemprop="name"]')
    eco_products_page.open()
    eco_products_page.choose_eco_product(name)
    product_page.open_eco_product(eco_products_page.eco_product_page_url)
    product_page.check_opened_correct_product_page(locator, name)


def test_unverified_adding_to_favorite(driver, eco_products_page, login_page):
    locator = ('xpath', f'//a[contains(text(), "{name}")]')
    eco_products_page.open()
    eco_products_page.move_attention(driver, locator)
    eco_products_page.click_to_favorite((locator[0], f'{locator[1]}/following::a[@data-action="add-to-wishlist"]'))
    assert login_page.check_unverified_action_opened(('xpath', '//div[@data-ui-id="message-error"]/div'))


def test_sorting_by_price(eco_products_page):
    eco_products_page.open()
    eco_products_page.sorting_by_('//select[@id="sorter"]', '//option[@value="price"]')
    assert eco_products_page.check_order_by_price('//span[@class="price"]')


def test_sales_page_opened(sales_page):
    sales_page.open()
    assert sales_page.check_sale_page_opened()


def test_luma_gear_offer(sales_page, deals_page):
    text = 'Gear'
    sales_page.open()
    sales_page.go_to_deal_page(text)
    assert deals_page.check_opened_correct_page(text)


def test_men_offer(sales_page, deals_page):
    text = 'Men'
    sales_page.open()
    sales_page.go_to_deal_page(text)
    assert deals_page.check_opened_correct_page(text)


def test_women_offer(sales_page, deals_page):
    sales_page.open()
    sales_page.go_to_deal_page('Pristine prices on pants, tanks and bras')
    assert deals_page.check_opened_correct_page('Women')

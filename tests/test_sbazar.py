def test_open_main_page(open_main_page):
    open_main_page.open()
    assert open_main_page.is_title_correct()
    assert open_main_page.is_text_present()

def test_changing_region(open_main_page, prague_page):
    open_main_page.open()
    open_main_page.changing_region()
    assert prague_page.is_text_present()
    assert prague_page.is_localized_text_present()


def test_sorting_products(open_main_page):
    open_main_page.open()
    open_main_page.sorting_by_('price', 'desc')
    assert open_main_page.is_sorting_correct()

def test_back_to_home_page_by_logo(open_main_page, prague_page):
    prague_page.open_prague_page()
    prague_page.click_to_logo_to_switch_to_main()
    assert open_main_page.is_title_correct()
    assert open_main_page.is_text_present()

def test_open_sport_supplies_page(sport_page):
    sport_page.open_sport_supplies_page()
    assert sport_page.is_title_correct()

def test_open_deeper_sport_supplies_page(another_sport_supply_page):
    another_sport_supply_page.open_another_sport_supplies_page()
    assert another_sport_supply_page.is_title_correct()

def test_open_account_help_page(open_main_page, signin_modal_window):
    open_main_page.open()
    open_main_page.click_to_login_lnk()
    signin_modal_window.open_help()
    assert signin_modal_window.check_correct_page_is_open()

def test_registration_form(open_main_page, signin_modal_window):
    open_main_page.open()
    open_main_page.click_to_login_lnk()
    signin_modal_window.click_create_new_account()
    signin_modal_window.choose_email_creation_link()
    signin_modal_window.enter_email()
    # signin_modal_window.fill_account_creating_form()

# def test_linkedin(linkedin):
#     linkedin.open_linkedin()

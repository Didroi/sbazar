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



from time import sleep

def test_open_main_page(open_main_page):
    open_main_page.open()
    assert open_main_page.is_title_correct()
    assert open_main_page.is_text_present()

def test_changing_region(open_main_page):
    open_main_page.open()
    open_main_page.changing_region()
    sleep(3)


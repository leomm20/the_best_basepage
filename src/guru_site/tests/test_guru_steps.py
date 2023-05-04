from src.guru_site.pages.guru_page import GuruPage


def test_prueba():
    g = GuruPage('chrome', highlight=True)
    g.navigate_to_guru()
    g.click_right()
    g.sleep(5)
    assert 'Edit' == g.get_result_right_click()
    g.click_ctx()
    g.sleep(1)
    g.accept_alert()
    g.sleep(1)
    g.click_double_click()
    g.sleep(1)
    g.accept_alert()
    g.sleep(1)
    g.close_browser()
    del g

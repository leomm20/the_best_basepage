from src.guru_site.pages.guru_page import GuruPage


def test_prueba():
    g = GuruPage('chrome', highlight=True)
    g.navigate_to_guru()
    g.right_click_me()
    g.sleep(5)
    assert 'Edit' == g.get_result_right_click()
    g.click_on_edit()
    g.sleep(1)
    g.accept_alert()
    g.sleep(1)
    g.double_click_me_to_see_alert()
    g.sleep(1)
    g.accept_alert()
    g.sleep(1)
    g.close_browser()
    del g

from src.pages.testing_site.testing_page import TestingPage
#
#
# @pytest.mark.regression
# def test_google_page():
#     g = GooglePage(driver)
#     g.navigate_to_google()
#     g.enter_search_criteria('Google')
#     g.click_google_search()
#     assert g.get_first_result() == 'Google'
#
#
# @pytest.mark.smoke
# def test_google_page_error():
#     g = GooglePage(driver)
#     g.navigate_to_google()
#     g.enter_search_criteria('Google')
#     g.click_google_search()
#     assert not g.get_first_result() == 'aaoogle'
#
#
# @pytest.mark.regression
# @pytest.mark.smoke
# def test_google_page_error2():
#     g = GooglePage(driver)
#     g.navigate_to_google()
#     g.enter_search_criteria('Google')
#     g.click_google_search()
#     assert not g.get_first_result() == 'aaoogle'


def test_prueba():
    t = TestingPage('chrome', highlight=True)
    t.navigate_to_testing()
    t.select_category("Básquetbol")
    t.sleep(1)
    t.click_btn_enviar()
    # si tenés 1 sola abierta, es la 0; como querés ir a la segunda, tenés que pasar 1 como argumento
    print('\n\n##############\n', t.get_title(), '\n##############\n')
    t.switch_to_window(1)
    print('\n\n##############\n', t.get_title(), '\n##############\n')
    assert 'Básquetbol' == t.get_result(1, 2)
    t.close_browser()

#  para ejecutar:
#  - nombre del archivo .py debe comenzar con test_, al igual que las funciones
#  pytest -v para que ejecute todos los tests
#  pytest -v -m [marcador] para que ejecute solo algunos
#      ejemplo:
#      pytest -v -m "regression or smoke"
#      va a ejecutar todos los tests que tengan esos marcadores
#
#  pytest --debug realiza inspección y genera archivo pytestdebug.log (atención! en nueva corrida se pisará la info)

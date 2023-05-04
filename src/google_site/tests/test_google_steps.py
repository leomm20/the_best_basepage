import pytest
from src.google_site.pages.google_page import GooglePage


@pytest.mark.regression
@pytest.mark.smoke
def test_prueba_ok():
    g = GooglePage('chrome', highlight=True)
    g.navigate_to_google()
    g.enter_search_criteria('Google')
    print('\nESTA ES LA PAGINA QUE SE PROBÓ:', g.current_url())
    g.maximize()
    g.highlight_web_element(g.find(g.btn_search))
    g.sleep(5)
    g.click_google_search()
    assert g.get_first_result() == 'Google'
    g.close_browser()
    del g


@pytest.mark.regression
def test_prueba_error():
    g = GooglePage('chrome', highlight=True)
    g.navigate_to_google()
    g.enter_search_criteria('Google')
    print('\nESTA ES LA PAGINA QUE SE PROBÓ:', g.current_url())
    g.maximize()
    g.highlight_web_element(g.find(g.btn_search))
    g.sleep(5)
    g.click_google_search()
    assert not g.get_first_result() == 'aaoogle'
    g.close_browser()
    del g


#  para ejecutar:
#  - nombre del archivo .py debe comenzar con test_, al igual que las funciones
#  pytest -v para que ejecute todos los tests
#  pytest -v -m [marcador] para que ejecute solo algunos
#      ejemplo:
#      pytest -v -m "regression or smoke"
#      va a ejecutar todos los tests que tengan esos marcadores
#
#  pytest --debug realiza inspección y genera archivo pytestdebug.log (atención! en nueva corrida se pisará la info)

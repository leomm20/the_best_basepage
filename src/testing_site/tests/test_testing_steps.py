from src.testing_site.pages.testing_page import TestingPage


def test_prueba():
    t = TestingPage('chrome', highlight=True)
    t.navigate_to_testing()
    t.select_category("Básquetbol")
    t.sleep(1)
    t.click_btn_enviar()
    # si tenés 1 sola abierta, es la 0; como querés ir a la segunda, tenés que pasar 1 como argumento
    print('\n\n############## Tab:', t.get_title(), '##############\n')
    t.switch_to_window(1)
    print('\n############## Tab:', t.get_title(), '##############\n')
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

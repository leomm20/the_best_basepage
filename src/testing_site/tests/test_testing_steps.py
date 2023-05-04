from src.testing_site.pages.testing_page import TestingPage


def test_prueba():
    t = TestingPage('chrome', highlight=True)
    t.navigate_to(t.url)
    # t.scroll_down("300")
    t.scroll_to_element(t.combo_deportes)
    t.sleep(1)
    t.select_from_dropdown_by_text(t.category_dropdown, 'Básquetbol')
    t.sleep(1)
    t.click_element(t.btn_enviar)
    # si tenés 1 sola abierta, es la 0; como querés ir a la segunda, tenés que pasar 1 como argumento
    print('\n\n############## Tab:', t.get_title(), '##############\n')
    t.switch_to_window(1)
    print('\n############## Tab:', t.get_title(), '##############\n')
    assert 'Básquetbol' == t.get_value_from_table(t.tabla_final, 1, 2)
    t.take_screenshot(t.get_title())
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

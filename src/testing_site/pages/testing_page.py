from src.the_best_basepage import BasePage as bp # , by


class TestingPage(bp):

    bla = (bp.XPATH, '//*[@id="examples"]/div[1]/div/form/p/select')
    category_dropdown = (by.XPATH, '//*[@id="examples"]/div[1]/div/form/p/select')
    btn_enviar = (by.XPATH, '//*[@id="examples"]/div[1]/div/form/p/input')
    combo_deportes = (by.XPATH, '//*[@id="examples"]/div[1]/div/form/p/select')

    # PARA TABLAS, NO USAR "By", sólo pasar string de XPATH, porque luego se completará con row y column
    tabla_final = '/html/body/table[1]'
    url = "https://www.htmlquick.com/es/reference/tags/select.html"

from selenium.webdriver.common.by import By
from src.the_best_basepage import BasePage


class TestingPage(BasePage):

    category_dropdown = (By.XPATH, '//*[@id="examples"]/div[1]/div/form/p/select')
    btn_enviar = (By.XPATH, '//*[@id="examples"]/div[1]/div/form/p/input')
    combo_deportes = (By.XPATH, '//*[@id="examples"]/div[1]/div/form/p/select')
    # PARA TABLAS, NO USAR "By", sólo pasar string de XPATH, porque luego se completará con row y column
    tabla_final = '/html/body/table[1]'
    url = "https://www.htmlquick.com/es/reference/tags/select.html"


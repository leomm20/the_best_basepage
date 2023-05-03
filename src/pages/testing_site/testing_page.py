from selenium.webdriver.common.by import By
from src.pages.base_page.the_best_basepage import BasePage


class TestingPage(BasePage):
    category_dropdown = (By.XPATH, '//*[@id="examples"]/div[1]/div/form/p/select')
    btn_enviar = (By.XPATH, '//*[@id="examples"]/div[1]/div/form/p/input')
    combo_deportes = (By.XPATH, '//*[@id="examples"]/div[1]/div/form/p/select')
    # PARA TABLAS, NO USAR "By", sólo pasar string de XPATH, porque luego se completará con row y column
    tabla_final = '/html/body/table[1]'

    def navigate_to_testing(self):
        self.navigate_to("https://www.htmlquick.com/es/reference/tags/select.html")

    def select_category(self, category):
        # self.scroll_down("300")
        self.scroll_to_element(self.combo_deportes)
        self.sleep(1)
        self.select_from_dropdown_by_text(self.category_dropdown, category)
        self.sleep(1)

    def click_btn_enviar(self):
        self.click_element(self.btn_enviar)

    def get_result(self, str_row, str_column):
        return self.get_value_from_table(self.tabla_final, str_row, str_column)

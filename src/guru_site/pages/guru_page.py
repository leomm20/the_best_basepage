from selenium.webdriver.common.by import By
from src.the_best_basepage import BasePage


class GuruPage(BasePage):
    btn_right_click = (By.XPATH, '//*[@id="authentication"]/span')
    btn_double_click = (By.XPATH, '//*[@id="authentication"]/button')
    ctx_edit = (By.XPATH, '//*[@id="authentication"]/ul/li[1]/span')

    def navigate_to_guru(self):
        self.navigate_to("https://demo.guru99.com/test/simple_context_menu.html")

    def click_right(self):
        self.right_click(self.btn_right_click)

    def get_result_right_click(self):
        return self.get_text(self.ctx_edit)

    def click_ctx(self):
        self.click_element(self.ctx_edit)

    def click_double_click(self):
        self.double_click(self.btn_double_click)

from selenium.webdriver.common.by import By
from src.the_best_basepage import BasePage


class GooglePage(BasePage):
    txt_search_text = (By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
    btn_search = (By.XPATH, "//input[@value='Buscar con Google']")
    first_result = (By.CSS_SELECTOR, "h3")

    def navigate_to_google(self):
        self.navigate_to("https://www.google.com")

    def enter_search_criteria(self, criteria):
        # self.write(self.txt_search_text, criteria)  # base_page_ori
        self.set_text(self.txt_search_text, criteria)

    def click_google_search(self):
        self.click_element(self.btn_search)

    def get_first_result(self):
        # return self.text_from_element(self.first_result)  # base_page_ori
        return self.get_text(self.first_result)

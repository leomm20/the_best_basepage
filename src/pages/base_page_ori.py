from webdriver_auto_update import check_driver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pathlib import Path
import os

# pip install selenium
# pip install webdriver-auto-update
# https://chromedriver.chromium.org/downloads

# MÉTODOS ESTÁNDAR


class BasePage:
    check_driver(str(Path(os.getcwd()).parent))

    # PROXY = "11.456.448.110:8080"
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server=%s' % PROXY)
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # para eliminar msg de USB
    chrome_options.add_experimental_option('excludeSwitches', ['disable-logging'])
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    def navigate_to(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def click_element(self, locator):
        self.find(locator).click()

    def write(self, locator, text_to_write):
        self.find(locator).clear()
        self.find(locator).send_keys(text_to_write)

    def text_from_element(self, locator):
        return self.find(locator).text

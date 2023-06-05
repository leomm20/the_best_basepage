import time
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest


@allure.severity(allure.severity_level.NORMAL)
class TestHRM:
    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(3)
        status = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[1]/img')\
            .is_displayed()
        if status:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='testLoginScreen',
                          attachment_type=AttachmentType.PNG)
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployees(self):
        pytest.skip('Skipping test... Later I will implement...')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name='testLogon',
                      attachment_type=AttachmentType.PNG)
        self.driver.close()
        assert False


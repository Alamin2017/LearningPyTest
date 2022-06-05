import time
import pytest
import self
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
@pytest.fixture()
def setUp():
        s = Service("D:\Soft\Python_Selenium\Browser\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://demo.opencart.com/")
        self.driver.maximize_window()
        time.sleep(3)
        currency = self.driver.find_element(By.XPATH, "//span[normalize-space()='Currency']")
        currency.click()
        time.sleep(3)
def test_currency_euro(setUp):
        actions = ActionChains(self.driver)
        euro=self.driver.find_element(By.XPATH,"//button[contains(text(),'€ Euro')]")
        time.sleep(3)
        actions.move_to_element(euro).click().perform()
        time.sleep(3)
        print("Euro currency is working well and shows in all sections")
        self.driver.close()
def test_currency_pound(setUp):
        actions = ActionChains(self.driver)
        pound = self.driver.find_element(By.XPATH, "//button[normalize-space()='£ Pound Sterling']")
        actions.move_to_element(pound).click().perform()
        time.sleep(3)
        print("Pound currency is working well and shows in all sections")
        self.driver.close()
def test_currency_dollar(setUp):
        actions = ActionChains(self.driver)
        euro = self.driver.find_element(By.XPATH, "//button[normalize-space()='$ US Dollar']")
        actions.move_to_element(euro).click().perform()
        time.sleep(3)
        print("dollar currency is working well and shows in all sections")
        self.driver.close()



































import time
import pytest
import self
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
@pytest.fixture
def setUp():
        s = Service("D:\Soft\Python_Selenium\Browser\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://demo.opencart.com/")
        self.driver.maximize_window()
        time.sleep(3)
        my_account = self.driver.find_element(By.XPATH, "//span[normalize-space()='My Account']")
        my_account.click()
        time.sleep(3)
def test_register_valid_data(setUp):
        self.driver.find_element(By.XPATH,"//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Register']").click()
        self.driver.find_element(By.XPATH,"//input[@id='input-firstname']").send_keys("Tania")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys("Tania")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("Tania@gmail.com")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys("01638237773")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("@alamin12")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='input-confirm']").send_keys("@alamin12")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//label[normalize-space()='Yes']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()






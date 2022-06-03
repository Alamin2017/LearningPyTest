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
def test_contact_us(setUp):
        number_format=self.driver.find_element(By.XPATH,"//span[normalize-space()='123456789']")
        if number_format.text=="123456789":
                assert True
        else:
                assert False
        contact_us=self.driver.find_element(By.XPATH,"//i[@class='fa fa-phone']")
        contact_us.click()
        time.sleep(3)
        print("Go to the Contact Us page")
        time.sleep(3)
        self.driver.close()
def test_about_us(setUp):
        time.sleep(3)
        about_us=self.driver.find_element(By.XPATH,"//a[normalize-space()='About Us']")
        time.sleep(3)
        self.driver.execute_script("arguments[0].scrollIntoView();", about_us)
        about_us.click()
        print("Go to the About Us page")
        time.sleep(3)
def test_Delivery_Information(setUp):
        time.sleep(3)
        Delivery_Information=self.driver.find_element(By.XPATH,"//a[normalize-space()='Delivery Information']")
        time.sleep(3)
        self.driver.execute_script("arguments[0].scrollIntoView();", Delivery_Information)
        Delivery_Information.click()
        print("Go to the Delivery Information page")
        time.sleep(3)
def test_Privacy_Policy(setUp):
        time.sleep(3)
        Privacy_Policy=self.driver.find_element(By.XPATH,"//a[normalize-space()='Privacy Policy']")
        time.sleep(3)
        self.driver.execute_script("arguments[0].scrollIntoView();", Privacy_Policy)
        Privacy_Policy.click()
        print("Go to the Privacy_Policy page")
        time.sleep(3)
def test_Terms_Conditions(setUp):
        time.sleep(3)
        Terms_Conditions=self.driver.find_element(By.XPATH,"//a[normalize-space()='Terms & Conditions']")
        time.sleep(3)
        self.driver.execute_script("arguments[0].scrollIntoView();", Terms_Conditions)
        Terms_Conditions.click()
        print("Go to the Terms_Conditions page")
        time.sleep(3)

def test_url_page_title(setUp):
        print(" "+self.driver.title)
        print(" "+self.driver.current_url)

def test_brand_footer(setUp):
        brand=self.driver.find_element(By.XPATH,"//a[normalize-space()='Brands']")
        time.sleep(3)
        self.driver.execute_script("arguments[0].scrollIntoView();",brand)
        time.sleep(3)
        brand.click()
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Apple']").click()
        time.sleep(3)
        macbook_air=self.driver.find_element(By.XPATH,"//img[@title='MacBook Air']")
        self.driver.execute_script("arguments[0].scrollIntoView();", macbook_air)
        time.sleep(3)
        macbook_air.click()
        self.driver.find_element(By.XPATH,"//button[@id='button-cart']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//strong[normalize-space()='Checkout']").click()
        time.sleep(3)







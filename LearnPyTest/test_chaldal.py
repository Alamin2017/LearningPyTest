import time
import pytest
import self
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture
def set_up_env_open_url():
    option = Options()
    option.add_argument('--disable-notifications')
    s = Service("D:\Soft\Python_Selenium\Browser\chromedriver.exe")
    self.driver = webdriver.Chrome(service=s,chrome_options=option)
    self.driver.maximize_window()
    self.driver.get("https://chaldal.com/")
    time.sleep(3)
def test_logo_image(set_up_env_open_url):
    image=self.driver.find_element(By.XPATH,"//*[@id='page']/div/div[3]/div/div[1]/div[1]/div[1]/a/img")
    print("Image is visible:",image.is_displayed())
    time.sleep(3)
def test_sign_in(set_up_env_open_url):
    self.driver.find_element(By.XPATH,"//button[normalize-space()='Sign in']").click()
    time.sleep(3)
    number=self.driver.find_element(By.XPATH,"//*[@id='page']/div/div[1]/div/div/div/div[2]/div/form/div[1]/div/div[1]/input")
    number.send_keys("01629674872")
    time.sleep(3)
    signin_button=self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/button[1]")
    signin_button.click()
    time.sleep(30)
    self.driver.find_element(By.XPATH,"//*[@id='page']/div/div[1]/div/div/div/div[2]/div/form/div[3]/button[1]").click()
    time.sleep(2)
def test_help_menu(set_up_env_open_url):
    time.sleep(5)
    self.driver.find_element(By.XPATH,"//*[@id='page']/div/div[3]/div/div[1]/div[1]/div[3]/a/span").click()
    time.sleep(5)
    self.driver.back()
def test_search_product(set_up_env_open_url):
    self.driver.find_element(By.XPATH,"//input[@name='search_term_string']").send_keys("potato",Keys.ENTER)
    time.sleep(3)
def test_product_details_add_to_cart(set_up_env_open_url):
    self.driver.find_element(By.XPATH, "//input[@name='search_term_string']").send_keys("potato",Keys.ENTER)
    time.sleep(3)
    self.driver.implicitly_wait(10)
    self.driver.find_element(By.XPATH,"//*[@id='page']/div/div[5]/section/div/div/div/div/section/div[2]/div[2]/div[1]/div/div").click()
    time.sleep(3)
    self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[5]/section/div/div/div/div/section/div[2]/div[2]/div[1]/div/div[1]/div[5]/span/a[1]/span[1]").click()
    time.sleep(3)
    element=self.driver.find_element(By.XPATH,"//*[@id='page']/div/div[5]/section/div/div/div/div/section/div[2]/div[2]/div[1]/div/div[3]/div")
    element.location_once_scrolled_into_view



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
def test_sign_in_number_out(set_up_env_open_url):
    self.driver.find_element(By.XPATH,"//button[normalize-space()='Sign in']").click()
    time.sleep(3)
    number=self.driver.find_element(By.XPATH,"//*[@id='page']/div/div[1]/div/div/div/div[2]/div/form/div[1]/div/div[1]/input")
    number.send_keys("01629674872")
    time.sleep(3)
    signin_button=self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/button[1]")
    signin_button.click()
    time.sleep(30)
    self.driver.find_element(By.XPATH,"//*[@id='page']/div/div[1]/div/div/div/div[2]/div/form/div[3]/button[1]").click()
    time.sleep(5)
    info_bar = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[5]")
    actions = ActionChains(self.driver)
    actions.move_to_element(info_bar).perform()
    time.sleep(5)
    self.driver.find_element(By.XPATH,"//div[@class='isLoggedIn top-header']//li[6]").click()
    time.sleep(5)

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
    time.sleep(3)
    buy_button=self.driver.find_element(By.XPATH,"//button[@id='buyNowButton']")
    buy_button.click()
    time.sleep(3)
    place_order=self.driver.find_element(By.XPATH,"//*[@id='placeOrderButton']/span[1]")
    place_order.click()
    time.sleep(3)
    close_place_order=self.driver.find_element(By.XPATH,"//*[@id='page']/div/div[2]/div/div[2]/div[1]/button")
    close_place_order.click()
    time.sleep(3)
    item_order=self.driver.find_element(By.XPATH,"//section[@class='stickyHeader']//div[@class='itemCount']")
    item_order.click()
    time.sleep(3)
    close_place_order.click()
def test_change_Language(set_up_env_open_url):
    time.sleep(3)
    self.driver.find_element(By.XPATH,"//p[contains(text(),'বাং')]").click()
    time.sleep(3)
    self.driver.find_element(By.XPATH,"//p[contains(text(),'EN')]").click()
def test_location_change_city(set_up_env_open_url):
    time.sleep(3)
    position=self.driver.find_element(By.XPATH,"//*[@id='page']/div/div[3]/div/div[1]/div[1]/div[2]/div[1]")
    actions = ActionChains(self.driver)
    actions.move_to_element(position).perform()
    time.sleep(3)
    self.driver.find_element(By.XPATH,"//*[@id='page']/div/div[3]/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/p").click()
    time.sleep(3)
    self.driver.find_element(By.XPATH,"//div[@id='1']//img[@class='cityImage']").click()
def test_Terms_of_Service(set_up_env_open_url):
    self.driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
    time.sleep(3)
    self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[4]/h5/a[2]").click()
    handles = self.driver.window_handles
    child=self.driver.window_handles[1]
    self.driver.switch_to.window(child)
    time.sleep(12)
    self.driver.close()
def test_Privacy_Policy(set_up_env_open_url):
    self.driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
    time.sleep(3)
    self.driver.find_element(By.LINK_TEXT,"Privacy Policy").click()
    handles = self.driver.window_handles
    child=self.driver.window_handles[1]
    self.driver.switch_to.window(child)
    time.sleep(12)
    self.driver.close()

def test_popular_product(set_up_env_open_url):
    time.sleep(3)
    self.driver.find_element(By.XPATH,"//a[contains(text(),'Popular')]").click()
    time.sleep(3)
    count=0
    products=self.driver.find_elements(By.XPATH,"//*[@class='productPane']/div")
    for p in products:
        print(p.text)
        print("")
        count=count+1
    print("Total Product Items:",+count)




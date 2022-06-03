import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class TestHRM:

    def test_logo(self):
        s=Service("D:\Soft\Python_Selenium\Browser\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        status = self.driver.find_element(By.XPATH, "//div[@id='divLogo']/img").is_displayed()
        time.sleep(3)
        if status == True:
            assert True
            self.driver.close()
        else:
            assert False
    def test_Login_Logout(self):
        s = Service("D:\Soft\Python_Selenium\Browser\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        time.sleep(3)
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        time.sleep(3)
        self.driver.find_element(By.ID, "btnLogin").click()
        time.sleep(3)

        act_title = self.driver.title

        if act_title == "OrangeHRM":
            assert True
        else:
            assert False

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@id='welcome']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()
        time.sleep(3)
        self.driver.close()



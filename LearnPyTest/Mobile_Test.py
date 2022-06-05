import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from self import self
def test_open_app():
        desired_cap = {
            "app": "D:\\Soft\\Android_Studio\\ApiDemos-debug.apk",
            "platformName": "Android",
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

def test_text_click():
        self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='Text']").click()

def test_marquee_click():
        self.driver.find_element(By.XPATH, "//android.widget.TextView[@content-desc='Marquee']").click()







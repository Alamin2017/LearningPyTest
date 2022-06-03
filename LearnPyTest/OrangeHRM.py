import time
import pytest
import self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.fixture

def setUp():
    s = Service("D:\Soft\Python_Selenium\Browser\chromedriver.exe")
    self.driver = webdriver.Chrome(service=s)
    self.driver.get("https://opensource-demo.orangehrmlive.com/")
    self.driver.maximize_window()

def test_logo(setUp):
    time.sleep(3)
    status = self.driver.find_element(By.XPATH, "//div[@id='divLogo']/img").is_displayed()
    time.sleep(3)
    if status == True:
        assert True
        self.driver.close()
    else:
        assert False


def test_Login_Logout(setUp):
    self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
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


def test_assign_leave(setUp):
    self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
    self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
    time.sleep(3)
    self.driver.find_element(By.ID, "btnLogin").click()
    time.sleep(3)

    self.driver.find_element(By.XPATH, "//span[normalize-space()='Assign Leave']").click()
    time.sleep(3)

    leave_type_dropdown = self.driver.find_element(By.XPATH, "//select[@id='assignleave_txtLeaveType']")
    drp_d = Select(leave_type_dropdown)
    drp_d.select_by_value("7")
    time.sleep(3)

    self.driver.find_element(By.XPATH, "//input[@id='assignleave_txtFromDate']").click()
    time.sleep(3)

    self.driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/select[1]").click()
    time.sleep(3)
    month = self.driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/select[1]")
    month_sel = Select(month)
    month_sel.select_by_value("10")
    time.sleep(3)

    self.driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/select[2]").click()
    time.sleep(3)
    year = self.driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/select[2]")
    year_sel = Select(year)
    year_sel.select_by_value("2020")
    time.sleep(3)

    all_dates = self.driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td")
    for i in all_dates:
        print(i.text)
    self.driver.find_element(By.XPATH, "//a[normalize-space()='20']").click()
    time.sleep(3)

    self.driver.find_element(By.XPATH, "//*[@id='assignleave_duration_duration']").click()
    leave_time_dropdown = self.driver.find_element(By.XPATH, "//*[@id='assignleave_duration_duration']")
    drp_t = Select(leave_time_dropdown)
    drp_t.select_by_value("full_day")
    time.sleep(3)
    self.driver.find_element(By.XPATH, "//textarea[@id='assignleave_txtComment']").send_keys("For Back pain")
    time.sleep(3)
    self.driver.find_element(By.XPATH, "//input[@id='assignleave_txtEmployee_empName']").send_keys("Odis Adalwin")
    time.sleep(3)
    self.driver.find_element(By.XPATH, "//input[@id='assignBtn']").click()
    time.sleep(3)

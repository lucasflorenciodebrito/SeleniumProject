from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")

#wait
driver.implicitly_wait(10) #seconds

assert "Welcome: Mercury Tours" in driver.title

user_element = driver.find_element_by_name("userName")
pwd_element = driver.find_element_by_name("password")
user_element.send_keys("mercury")
pwd_element.send_keys("mercury")
driver.find_element_by_name("submit").click()
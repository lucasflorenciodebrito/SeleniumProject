from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
driver.get("http://google.com")
print(driver.title)
driver.get("http://pavantestingtools.blogspot.in/")
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)
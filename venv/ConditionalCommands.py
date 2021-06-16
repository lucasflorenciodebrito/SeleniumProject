from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
user_element = driver.find_element_by_name("userName")

print(user_element.is_displayed()) # returns true/false based on element status
print(user_element.is_enabled())

pwd_element = driver.find_element_by_name("password")
print(pwd_element.is_displayed()) # returns true/false based on element status
print(pwd_element.is_enabled())

user_element.send_keys("mercury")
pwd_element.send_keys("mercury")
driver.find_element_by_name("submit").click()

driver.get("http://demo.guru99.com/test/newtours/reservation.php")
roundtrip_radio = driver.find_element_by_css_selector("input[value = roundtrip]")
print("status of round trip radio button:" , roundtrip_radio.is_selected())  #print status of roundtrip radio button

onetrip_radio = driver.find_element_by_css_selector("input[value = oneway]")
print("status of onetrip radio button:", onetrip_radio.is_selected())

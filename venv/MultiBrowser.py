from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\Driver\geckodriver.exe")

driver.maximize_window()
driver.get("http://demo.guru99.com/test/newtours/")
print(driver.title) #Title of the page
print(driver.current_url) #Returns the URL of the page
#print(driver.page_source) #HTML code for the page
driver.close() # close the browser
import time

from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time
driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title) #eturns title of the page
print(driver.current_url)  #returns URL of the page
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)
driver.quit() #close all the windows

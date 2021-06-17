import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.expedia.com")

driver.find_element_by_link_text("Flights").click() #Flights button

time.sleep(2) #from python

driver.find_element_by_css_selector(".has-no-placeholder > .uitk-faux-input").click()

wait = WebDriverWait(driver,10)
element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class= 'uitk-field has-no-visible-label has-placeholder']/input")))

element.send_keys('SFO')

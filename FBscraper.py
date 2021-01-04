from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

import time
from bs4 import BeautifulSoup

import os
from dotenv import load_dotenv

#Initialize Browser
driver = webdriver.Firefox()#You could also use chrome

wait = WebDriverWait(driver, 10)
driver.get("https://www.facebook.com")

load_dotenv()
userid = os.getenv('USER')
pwd = os.getenv('PASS')
time.sleep(5)

#Login To FB
emailelement= driver.find_element_by_xpath('.//*[@id="email"]')
emailelement.send_keys(userid)
passwordfield= driver.find_element_by_xpath('.//*[@id="pass"]')
passwordfield.send_keys(pwd)
#button= driver.find_element_by_xpath('.//*[@id="login"]')
button = driver.find_element_by_name('login')
button.click()
time.sleep(2)

driver.get("https://www.facebook.com/events/birthdays/")
time.sleep(5)

#element = driver.find_elements_by_xpath("//*[@class ='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']") 
soup = BeautifulSoup(driver.page_source,'lxml')
driver.quit()

with open("out1.html", "w+") as f:
    f.write(soup.prettify())
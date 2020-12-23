from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

import time
from bs4 import BeautifulSoup
import re

""" Will Implement Class object after completed prototyping
class Bot(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver,10)
    
    def get_bdays(self, uname, password):
        self.wait
        self.driver.get("https://www.facebook.com")
"""
driver = webdriver.Firefox()#You could also use chrome

wait = WebDriverWait(driver, 10)
driver.get("https://www.facebook.com")
userid = "username"
pwd = "password"
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

print(type(soup.prettify()))

json_objects = re.search('\{.*?\}', soup.prettify())
print(json_objects)

with open("out1.html", "w+") as f:
    f.write(soup.prettify())

#b_container = soup.find('div',{'id':'placeholder-8rmt0'})

#print(b_container)

#element = driver.find_elements_by_xpath("textarea")
#print(element)
#bdays = "d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v lrazzd5p oo9gr5id"
#bday="j83agx80.pybr56ya.rz4wbd8a.sj5x9vvc.a8nywdso"
#bday = 'tvmbv18p.s1tcr66n'
#container = driver.find_element_by_css_selector(bday)
#print(len(containers))
#birthdaystoday= containers[0]


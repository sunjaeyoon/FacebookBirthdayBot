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

import parser

def getHTML():
    driver = webdriver.Firefox()#You could also use chrome

    wait = WebDriverWait(driver, 10)
    driver.get("https://www.facebook.com")

    load_dotenv()
    userid = os.getenv('FACEBOOK_USER')
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

    soup = BeautifulSoup(driver.page_source,'lxml')
    driver.quit()

    return soup.prettify()

def today():
    import datetime
    dt = datetime.datetime.today()

    today_bday = []
    data = getHTML()
    json_bday = parser.getBdays(data)

    for person in json_bday:
        bday = person['birthdate']
        if bday['month'] == dt.month and bday['day'] == dt.day:
            print("Happy Birthday", person['name'])
            today_bday.append(person)
    
    return today_bday

if __name__ == "__main__":
    today()


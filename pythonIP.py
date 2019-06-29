from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os, json, getpass, time, random

options = Options()
options.add_argument('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
options.add_argument("--kiosk")

# kates ip
browser = webdriver.Chrome(options=options)
browser.get('http://13.59.186.14/')

# name = 'aaa'
# username = 'aaaa'
# pword = 'aaaaaaaa'
# cpword = pword

destination = 'Selenium City'
description = 'Ya been fooled'
start = '01/01/2021'
end = '01/02/2021'

logUser = 'testuser'
logPW = '932gfxyn78'

def reg():
    elem = browser.find_element_by_id('name')
    elem.send_keys(name)
    time.sleep(.1)
    elem = browser.find_element_by_id('exampleInputEmail1')
    elem.send_keys(username)
    time.sleep(.1)
    elem = browser.find_element_by_id('password')
    elem .send_keys(pword)
    time.sleep(.1)
    elem = browser.find_element_by_id('exampleInputPassword1')
    elem .send_keys(pword)

def login():
    elem = browser.find_element_by_name('login_username')
    elem.send_keys(logUser)
    elem = browser.find_element_by_name('login_password')
    elem.send_keys(logPW)
    browser.find_element_by_xpath('/html/body/div/div/div[2]/form/button').click()

def trip():
    c = browser.find_element_by_xpath('/html/body/div[1]/a[3]')
    time.sleep(.1)
    c.click()

    elem = browser.find_element_by_id('destination')
    elem.send_keys(destination)

    elem = browser.find_element_by_name('plan')
    elem.send_keys(description)

    elem = browser.find_element_by_id('start_date')
    elem.send_keys(start)

    elem = browser.find_element_by_name('end_date')
    elem.send_keys(end)

    browser.find_element_by_xpath('/html/body/div[2]/form/button').click()

def troll():
    login()
    while(True):
        trip()
    
troll()
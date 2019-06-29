from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os, json, getpass, time, random

options = Options()
options.add_argument('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
options.add_argument("--kiosk")

# elliots ip
browser = webdriver.Chrome(options=options)
browser.get('http://34.239.187.49/pets')


# names = ['Liam,Emma,Noah,Olivia,William,Ava,James,Isabella,Oliver,Sophia,Benjamin,Charlotte,Elijah,Mia,Lucas,Amelia,Mason,Harper,Logan,Evelyn']
name = 'selenium4'
petType = 'selenium'
description = 'selenium was here'
ran = random.randint(1,60)
# tableDetails = '//*[@id="root"]/div/div/table/tbody/tr[10]/td[3]/a[1]]'
# delButton = '//*[@id="root"]/div/div/div[2]/div[2]/button'
def createPet():
    time.sleep(.1)
    browser.find_element_by_link_text('Add a pet to the shelter').click()
    time.sleep(.1)
    elem = browser.find_element_by_xpath('//*[@id="root"]/div/div/form/div[1]/input')
    elem.send_keys(name)
    time.sleep(.1)
    elem = browser.find_element_by_xpath('//*[@id="root"]/div/div/form/div[2]/input')
    elem.send_keys(petType)
    time.sleep(.1)
    elem = browser.find_element_by_xpath('//*[@id="root"]/div/div/form/div[3]/input')
    elem.send_keys(description)
    time.sleep(.1)
    browser.find_element_by_xpath('//*[@id="root"]/div/div/form/input').click()


def delete():
    time.sleep(.1)
    elem = browser.find_element_by_xpath('//*[@id="root"]/div/div/table/tbody/tr[10]/td[3]/a[1]')
    time.sleep(.1)
    elem.send_keys(Keys.RETURN)
    time.sleep(.1)
    browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/button').click()

# infinitely inputs a new pet until the end of time
# while(True):
#     name += str(ran)
#     createPet()

while(True):
    delete()
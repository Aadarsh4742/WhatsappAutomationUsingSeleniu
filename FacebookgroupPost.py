import email
from itertools import dropwhile
from lib2to3.pgen2 import driver
from re import search
import selenium 
import imp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
import time

import pyperclip

#Importing time libraries to add wait times
from datetime import datetime
from time import sleep

#Options functionality to disable Notifications

Chrome_options = Options()

#Disable the notifications
Chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(executable_path='D:\Coding\Python\Automation\Drivers\chromedriver.exe', options=Chrome_options)
driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(2)

#Accept Cookies
#cookies =  WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="_42ft')))

with open('email.txt', 'r', encoding='utf8') as f:
    emaildet = f.read()

with open('pass1.txt', 'r', encoding='utf8') as f:
    pass1 = f.read()
    
search_xpath = '//*[@id="email"]'
search_box = WebDriverWait(driver, 5).until(
ec.presence_of_element_located((By.XPATH, search_xpath )))
search_box.clear()
    
time.sleep(1)
    
pyperclip.copy(emaildet)
    
search_box.send_keys(Keys.SHIFT, Keys.INSERT) #Keys.Control + v
    
time.sleep(3)

#search_box.send_keys(Keys.TAB)

#Pass details filing

pass_xpath = '//*[@id="pass"]'

pass_box = WebDriverWait(driver, 5).until(
ec.presence_of_element_located((By.XPATH, pass_xpath )))
pass_box.clear()
    
time.sleep(1)
    
pyperclip.copy(pass1)
    
search_box.send_keys(Keys.SHIFT, Keys.INSERT) #Keys.Control + v
    
time.sleep(3)

pass_box.send_keys(Keys.ENTER)


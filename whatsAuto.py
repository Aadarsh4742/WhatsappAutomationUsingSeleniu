from concurrent.futures import thread

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


driver = webdriver.Chrome(executable_path='D:\Coding\Python\Automation\Drivers\chromedriver.exe')

driver.maximize_window()

driver.get("https://web.whatsapp.com/")

with open('groups.txt', 'r', encoding='utf8') as f:
    groups = [group.strip() for group in f.readlines()]

with open('msg.txt', 'r', encoding='utf8') as f:
    msg = f.read()
# with open('msg.txt', 'r', encoding='utf8') as f:
#     msg1 = f.read()
    

for group in groups:
    search_xpath = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
    search_box = WebDriverWait(driver, 500).until(
        ec.presence_of_element_located((By.XPATH, search_xpath ))
    )
    search_box.clear()
    
    time.sleep(1)
    
    pyperclip.copy(group)
    
    search_box.send_keys(Keys.SHIFT, Keys.INSERT) #Keys.Control + v
    
    time.sleep(5)
    
    search_box.send_keys(Keys.ENTER)
    
    # group_xpath = '//span[@title="{group}"]'
    # group_title = driver.find_element(group_xpath)
    
    # group_title.onclick()
    
    
    time.sleep(5)
    
    input_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p     '
    # input_box = driver.find_element(input_xpath)

    input_box = WebDriverWait(driver, 3).until(
        ec.presence_of_element_located((By.XPATH, input_xpath))
    )
    input_box.clear()

    
    pyperclip.copy(msg)
    
    input_box.send_keys(Keys.SHIFT, Keys.INSERT)    #Keys.Control + v
    
    input_box.send_keys(Keys.ENTER)
    
    # time.sleep(3)
    # dataicon_xpath= '//*[@id="main"]/div[3]/div/div[2]/div[3]/div[37]/div/div[1]/div[1]/div[2]/div/div/span'
    # dataicon_value = driver.find_elements(dataicon_xpath).__getattribute__("data-icon")
    # 
    # while (True):
    #     if "check" in dataicon_value:
    #         quit()
    #     else:
    #         thread.sleep(1000)
    #         continue
quit()
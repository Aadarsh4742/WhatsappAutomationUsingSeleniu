import imp
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome(executable_path="D:\Coding\Python\Automation\chromedriver_win32\chromedriver.exe")
contact = "Aadarsh"
text = "Hey Bitchmagnet"

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
print("Scan QR Code and then Enter:")
input()
print("Logged in successfully")


inp_xpath_search = "//input[@title='Search or start new chat']"
input_box_search = WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact)
time.sleep(2)

#Command for clicking the contact which is found in the result 
selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()


#Finding the text box, enter the text and press enter automatically
inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
input_box.send_keys(text + Keys.ENTER)
time.sleep(2)


driver.quit()
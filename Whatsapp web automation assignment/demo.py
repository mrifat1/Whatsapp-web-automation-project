from openpyxl import load_workbook
import os,time,datetime
import time, os, platform
import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def msg():
    name  = input('\nInput the group/Username : ')
    message = input('Input Messages you want to send: ')
    count = int(input('count of message'))



lw = load_workbook(filename = 'data.xlsx')
data = lw.active

for i in data.index():
    number = str(lw['Phone Number'][i])
    print(number)

# coloumnumber = data['C']
# lst = []
# for cell in range(len(coloumnumber)):
#     contactnumber = str(coloumnumber[cell].value)
#     if contactnumber.isdigit():
#         lst.append(contactnumber)
#
#
#
#
# driver = webdriver.Chrome("chromedriver")
# driver.get("https://web.whatsapp.com")
# PHONE_NUMER_INPUT = "//*[@id='side']/div[1]/div/label/div/div[2]"
# SEND_BUTTON = "//*[@id='main']/footer/div[1]/div[2]/div/div[2]/button"
#

# driver.find_element_by_xpath(PHONE_NUMER_INPUT)







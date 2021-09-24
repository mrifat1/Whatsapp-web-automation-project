import os,time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

FILE_LOC = "data.xlsx"
SRNO = 'SRNO'
NAME = 'Name'
PHONENUMBER = 'Phone Number'
MESSAGE = 'Message'
URL = 'https://web.whatsapp.com/'
WAITER_ELEMENT = "landing-title _3-XoE"
PHONE_NUMER_INPUT = "//*[@id='side']/div[1]/div/label/div/div[2]"
MESSAGE_INPUT = "//*[@id='main']/footer/div[1]/div/div/div[2]/div[1]/div/div[2]"
SEND_BUTTON = "//*[@id='main']/footer/div[1]/div/div/div[2]/div[2]/button/span"
Three_dot = "//*[@id='side']/header/div[2]/div/span/div[3]/div/span"
Log_out = "//*[@id='side']/header/div[2]/div/span/div[3]/span/div[1]/ul/li[6]/div[1]"

dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = webdriver.ChromeOptions()
options.add_argument(
    r"user-data-dir={}".format(profile))

driver = webdriver.Chrome('chromedriver.exe',options=options)
driver.implicitly_wait(10)
waiter = WebDriverWait(driver, 10)
data = []

def read_data_from_excel():
    try:
        df = pd.read_excel(FILE_LOC)
        print("Retrieving data from excel")
    except:
        print("Excel 'data.xlsx' not found")
    print("Found {0} messages to be send".format(len(df.index)))
    for i in df.index:
        number = str(df[PHONENUMBER][i])
        output = {
            'SrNo': df[SRNO][i],
            'Name': df[NAME][i],
            'PhoneNumber': number,
            'Message': df[MESSAGE][i],
            'Message_check': df['Message_check'][i]
        }
        data.append(output)


def send_whatsapp_message():
    # global driver
    driver.get(URL)
    print("Loading site...")
    waiter.until(EC.title_is("WhatsApp"))
    print("Site loaded successfully...")
    print("Waiting for user to log in using WhatsApp Web")
    waitCounter = 0
    while 1:
        try:
            waiter.until(EC.presence_of_element_located((By.XPATH, "//canvas[@aria-label='Scan me!']")))
            waitCounter += 1
            if waitCounter % 1000 == 0:
                print("Waiting for user to log in...")
        except:
            print("Logged in to WhatsApp", 'INFO')
            break
    df = pd.read_excel(FILE_LOC)
    j = 1

    for entry in data:
        driver.find_element_by_xpath(PHONE_NUMER_INPUT).send_keys(str(entry['PhoneNumber']))
        time.sleep(2)

        driver.find_element_by_xpath(PHONE_NUMER_INPUT).send_keys(Keys.ENTER)
        time.sleep(1)
        for i in range(1):
            driver.find_element_by_xpath(MESSAGE_INPUT).send_keys(str(entry['Message']))
            time.sleep(2)
            driver.find_element_by_xpath(SEND_BUTTON).click()
            time.sleep(1)
        df['Message_check'] =('Sent')
        df.to_excel('new.xlsx')
        j+=1



def auto_logout():
    driver.find_element_by_xpath(Three_dot).click()
    time.sleep(1)
    driver.find_element_by_xpath(Log_out).click()
    time.sleep(1)



if __name__ == '__main__':

    read_data_from_excel()

    send_whatsapp_message()
    time.sleep(2)

    auto_logout()
    time.sleep(2)

    driver.close()
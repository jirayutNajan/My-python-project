from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
import sys
import random
from time import sleep

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
driver.get("https://10fastfingers.com/typing-test/english")

WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection"]')))
driver.find_element_by_xpath('//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection"]').click()

WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="row1"]/span[1]')))

run = True
i = 0
while run:
    i += 1 
    e = str(i)
    try:
        wrd = '//*[@id="row1"]/span['+e+']'
        word = driver.find_element_by_xpath(wrd)
        input_field = driver.find_element_by_xpath('//*[@id="inputfield"]')
        input_field.send_keys(word.text+' ')
    except:
        sleep(5)
        driver.quit()
        run = False
    sleep(0.15)

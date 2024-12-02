from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
import sys
from time import sleep

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
driver.get("https://10ff.net/login")

name = driver.find_element_by_xpath('//*[@id="username"]')
name.send_keys('dddd')
driver.find_element_by_xpath('//*[@id="auth"]/input[2]').click()

element = WebDriverWait(driver, 15).until(expected_conditions.invisibility_of_element_located((By.XPATH, '//*[@id="game"]/div[2]/div')))

run = True
i = 0
while run:
    i += 1 
    e = str(i)
    try:
        wrd = '//*[@id="game"]/div[3]/div[2]/div[1]/div/span['+e+']'
        word = driver.find_element_by_xpath(wrd)
        input_field = driver.find_element_by_xpath('//*[@id="game"]/div[3]/div[2]/div[2]/div[1]/input')
        input_field.send_keys(word.text+' ')
    except:
        sleep(5)
        driver.quit()
        run = False
    sleep(1.5)

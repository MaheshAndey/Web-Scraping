import scrapy
from scrapy.selector import Selector
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv


options = Options()
ser = Service("C:/Users/ramak/Downloads/chromedriver_win32 2/chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get('https://www.programiz.com/')

click_on_python = driver.find_element(By.XPATH, '//*[@id="node-368"]/div/div[1]/div[2]/div/div[2]/a[1]/div/h3')
click_on_python.click()

l = []

sub_topics = driver.find_elements(By.TAG_NAME, 'a')

sub_topics_1 = driver.find_elements(By.XPATH, '//*[@id="introduction"]/div/div/ul/li/a')
sub_topics_2 = driver.find_elements(By.XPATH, '//*[@id="flow-control"]/div/div/ul/li/a')
sub_topics_3 = driver.find_elements(By.XPATH, '//*[@id="functions"]/div/div/ul/li/a')
sub_topics_4 = driver.find_elements(By.XPATH, '//*[@id="datatypes"]/div/div/ul/li/a')
sub_topics_5 = driver.find_elements(By.XPATH, '//*[@id="files"]/div/div/ul/li/a')
sub_topics_6 = driver.find_elements(By.XPATH, '//*[@id="object-class"]/div/div/ul/li/a')
sub_topics_7 = driver.find_elements(By.XPATH, '//*[@id="advanced-topic"]/div/div/ul/li/a')
sub_topics_8 = driver.find_elements(By.XPATH, '//*[@id="date-time"]/div/div/ul/li/a')



j = 0
for i in sub_topics_1:
    j += 1
    driver.find_element(By.XPATH, '//*[@id="introduction"]/div/div/ul/li' + '[' + str(j) + ']' + '/a').click()
    n_p = driver.find_elements(By.TAG_NAME, 'p')
    n_h = driver.find_elements(By.TAG_NAME, 'h3')
    n_h1 = driver.find_elements(By.TAG_NAME, 'h1')
    n_li = driver.find_elements(By.TAG_NAME, 'li')
    n_code = driver.find_elements(By.TAG_NAME, 'code')

    ss = n_p + n_h + n_li + n_code + n_h1
    for i in ss:
        l+=str(i.text).split(" ")
    time.sleep(5)
    driver.back()

    e = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="introduction"]/div/div/ul/li' + '[' + str(j) + ']' + '/a'))
    )
    l += str(e.text).split(" ")
j = 0
for i in sub_topics_2:
    j += 1
    driver.find_element(By.XPATH, '//*[@id="flow-control"]/div/div/ul/li' + '[' + str(j) + ']' + '/a').click()
    n_p = driver.find_elements(By.TAG_NAME, 'p')
    n_h = driver.find_elements(By.TAG_NAME, 'h3')
    n_h1 = driver.find_elements(By.TAG_NAME, 'h1')
    n_li = driver.find_elements(By.TAG_NAME, 'li')
    n_code = driver.find_elements(By.TAG_NAME, 'code')

    ss = n_p + n_h + n_li + n_code + n_h1
    for i in ss:
        l+=str(i.text).split(" ")
    time.sleep(5)
    driver.back()

    e = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="flow-control"]/div/div/ul/li' + '[' + str(j) + ']' + '/a'))
    )
    l += str(e.text).split(" ")

j = 0
for i in sub_topics_3:
    j += 1
    driver.find_element(By.XPATH, '//*[@id="functions"]/div/div/ul/li' + '[' + str(j) + ']' + '/a').click()
    n_p = driver.find_elements(By.TAG_NAME, 'p')
    n_h = driver.find_elements(By.TAG_NAME, 'h3')
    n_h1 = driver.find_elements(By.TAG_NAME, 'h1')
    n_li = driver.find_elements(By.TAG_NAME, 'li')
    n_code = driver.find_elements(By.TAG_NAME, 'code')

    ss = n_p + n_h + n_li + n_code + n_h1
    for i in ss:
        l+=str(i.text).split(" ")
    time.sleep(5)
    driver.back()

    e = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="functions"]/div/div/ul/li' + '[' + str(j) + ']' + '/a'))
    )
    l += str(e.text).split(" ")


j = 0
for i in sub_topics_4:
    j += 1
    driver.find_element(By.XPATH, '//*[@id="datatypes"]/div/div/ul/li' + '[' + str(j) + ']' + '/a').click()
    n_p = driver.find_elements(By.TAG_NAME, 'p')
    n_h = driver.find_elements(By.TAG_NAME, 'h3')
    n_h1 = driver.find_elements(By.TAG_NAME, 'h1')
    n_li = driver.find_elements(By.TAG_NAME, 'li')
    n_code = driver.find_elements(By.TAG_NAME, 'code')

    ss = n_p + n_h + n_li + n_code + n_h1
    for i in ss:
        l+=str(i.text).split(" ")
    time.sleep(5)
    driver.back()

    e = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="datatypes"]/div/div/ul/li' + '[' + str(j) + ']' + '/a'))
    )
    l += str(e.text).split(" ")


j = 0
for i in sub_topics_5:
    j += 1
    driver.find_element(By.XPATH, '//*[@id="files"]/div/div/ul/li' + '[' + str(j) + ']' + '/a').click()
    n_p = driver.find_elements(By.TAG_NAME, 'p')
    n_h = driver.find_elements(By.TAG_NAME, 'h3')
    n_h1 = driver.find_elements(By.TAG_NAME, 'h1')
    n_li = driver.find_elements(By.TAG_NAME, 'li')
    n_code = driver.find_elements(By.TAG_NAME, 'code')

    ss = n_p + n_h + n_li + n_code + n_h1
    for i in ss:
        l+=str(i.text).split(" ")
    time.sleep(5)
    driver.back()

    e = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="files"]/div/div/ul/li' + '[' + str(j) + ']' + '/a'))
    )
    l += str(e.text).split(" ")


j = 0
for i in sub_topics_6:
    j += 1
    driver.find_element(By.XPATH, '//*[@id="object-class"]/div/div/ul/li' + '[' + str(j) + ']' + '/a').click()
    n_p = driver.find_elements(By.TAG_NAME, 'p')
    n_h = driver.find_elements(By.TAG_NAME, 'h3')
    n_h1 = driver.find_elements(By.TAG_NAME, 'h1')
    n_li = driver.find_elements(By.TAG_NAME, 'li')
    n_code = driver.find_elements(By.TAG_NAME, 'code')

    ss = n_p + n_h + n_li + n_code + n_h1
    for i in ss:
        l+=str(i.text).split(" ")
    time.sleep(5)
    driver.back()

    e = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="object-class"]/div/div/ul/li' + '[' + str(j) + ']' + '/a'))
    )
    l += str(e.text).split(" ")


j = 0
for i in sub_topics_7:
    j += 1
    driver.find_element(By.XPATH, '//*[@id="advanced-topic"]/div/div/ul/li' + '[' + str(j) + ']' + '/a').click()
    n_p = driver.find_elements(By.TAG_NAME, 'p')
    n_h = driver.find_elements(By.TAG_NAME, 'h3')
    n_h1 = driver.find_elements(By.TAG_NAME, 'h1')
    n_li = driver.find_elements(By.TAG_NAME, 'li')
    n_code = driver.find_elements(By.TAG_NAME, 'code')

    ss = n_p + n_h + n_li + n_code + n_h1
    for i in ss:
        l+=str(i.text).split(" ")
    time.sleep(5)
    driver.back()

    e = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="advanced-topic"]/div/div/ul/li' + '[' + str(j) + ']' + '/a'))
    )
    l += str(e.text).split(" ")


j = 0
for i in sub_topics_8:
    j += 1
    driver.find_element(By.XPATH, '//*[@id="date-time"]/div/div/ul/li' + '[' + str(j) + ']' + '/a').click()
    n_p = driver.find_elements(By.TAG_NAME, 'p')
    n_h = driver.find_elements(By.TAG_NAME, 'h3')
    n_h1 = driver.find_elements(By.TAG_NAME, 'h1')
    n_li = driver.find_elements(By.TAG_NAME, 'li')
    n_code = driver.find_elements(By.TAG_NAME, 'code')

    ss = n_p+n_h+n_li+n_code+n_h1
    for i in ss:
        l+=str(i.text).split(" ")
    time.sleep(5)
    driver.back()

    e = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="date-time"]/div/div/ul/li' + '[' + str(j) + ']' + '/a'))
    )
    l += str(e.text).split(" ")


l = list(set(l))


f = open("data.csv", "w")
header = ['S.No.', 'Word']

csvwriter = csv.writer(f)
csvwriter.writerow(header)
rows = []
for i in range(len(l)):
    rows.append([str(i), l[i]])
csvwriter.writerows(rows)




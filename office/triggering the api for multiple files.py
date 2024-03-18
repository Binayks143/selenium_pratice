import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import base_data
import os

URL="https://admin.smartcoin.co.in/"
# driver=webdriver.Chrome()
driver=webdriver.Chrome()

driver.get(URL)
driver.maximize_window()


user_name = driver.find_element(By.ID, "identifierId")
user_name.send_keys("binay.kumar@smartcoin.co.in")
time.sleep(2)
next = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
next.click()
time.sleep(2)

# importing password and encoding it

password = base_data.base_password
encoded_password = base64.b64encode(password.encode("utf-8"))

# finding the element and decoading password
password = driver.find_element(By.XPATH, "//input[@type='password']")
decode_password = base64.b64decode(encoded_password).decode("utf-8")
password.send_keys(decode_password)
next = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()
time.sleep(10)




folder_path = r"C:\Users\SC-229-USER\Desktop\test11"
files = os.listdir(folder_path)

for file_name in files:
    driver.get(URL + "redash_jobs/7586/uploadCsv")
    file_input = driver.find_element(By.NAME, "queryCsvFile")
    file_path = os.path.join(folder_path, file_name)
    file_input.send_keys(file_path)
    time.sleep(2)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(30)

# file_path = r"C:\Users\SC-229-USER\Desktop\test11\file_0.csv"

# Send the file path to the file input element
# file_input.send_keys(file_path)

# time.sleep(2)

'''
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//a[contains(text(),"Download Errors")]').click()
time.sleep(2)
'''
driver.quit()


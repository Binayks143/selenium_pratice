import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import base_data


URL="https://qa106-admin.rebase.in/"
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

driver.get(URL+"loan_products/insert-pa-lp")

time.sleep(2)
file_input=driver.find_element(By.ID,"file-upload")
file_path = r"C:\Users\SC-229-USER\Desktop\testCasesData.csv"

# Send the file path to the file input element
file_input.send_keys(file_path)

time.sleep(3)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//a[contains(text(),"Download Errors")]').click()
time.sleep(2)

driver.quit()


from selenium import webdriver
# from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import base64
import base_data
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# initialize a webdriver instance
driver = webdriver.Chrome()
driver.get("https://qa106-admin.rebase.in/")
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
print(encoded_password)
# finding the element and decoading password
password = driver.find_element(By.XPATH, "//input[@type='password']")
decode_password = base64.b64decode(encoded_password).decode("utf-8")
print(decode_password)
password.send_keys(decode_password)
next = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()
time.sleep(3)

# opening the routes file and reading the data
with open("routes", 'r') as routes_file:
    text = routes_file.read()

# converting row data into list
my_list = text.splitlines()
# print(my_list)

# creating URL with routes
urlList = []
URL = "https://qa106-admin.rebase.in/"
for uri1 in my_list:
    temp = str(uri1)
    urlList.append(temp)

for i in urlList:
    print(i)
# unique file name
base_file_name = "response_file"
time_stamp=int(time.time())*1000
filename=base_file_name+str(time_stamp)+str(".html")

# opening each URL in different tab
for uri in urlList:
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 't')
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(uri)
    # time.sleep(3)

    try:
        a = driver.find_element(By.XPATH, "//a[contains(text(),'Home')]")
        text = a.text
        if text=="Home":
            with open(filename, 'a') as response_file:
                # encode the string as bytes
                show_uri = uri
                response_file.write(show_uri)
                response_file.write('\n')
                # response_file.write(str(status_code))
                # response_file.write('\n')
                # response_file.write(str(response))
                # response_file.write('\n')
    except NoSuchElementException:
        with open(filename + "_temp", 'a') as response_file:
            # encode the string as bytes
            show_uri = uri
            response_file.write(show_uri)
            response_file.write('\n')






    # response = driver.execute_script("return document.documentElement.outerHTML;")
    # status_code = driver.execute_script("return window.performance.timing.responseEnd - window.performance.timing.requestStart;")


driver.quit()

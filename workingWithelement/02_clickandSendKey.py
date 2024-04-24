import base64
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from office import base_data


class ClickandSendkey():
    def login(self):
        baseurl="https://qa106-admin.rebase.in/"
        driver=webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(5)

        user_name = driver.find_element(By.ID, "identifierId")
        user_name.send_keys("binay.kumar@smartcoin.co.in")
        time.sleep(2)
        user_name.clear()
        time.sleep(2)
        user_name.send_keys("binay.kumar@smartcoin.co.in")

        next = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
        color = next.value_of_css_property("color")
        # This will return the value of the "color" CSS property for the specified element,
        # which could be in formats like hex, RGB, RGBA, or named colors depending on how
        # it's defined in the CSS.
        print(color)

        next.click()
        time.sleep(2)

        # importing password and encoding it

        password = base_data.base_password
        encoded_password = base64.b64encode(password.encode("utf-8"))

        # finding the element and decoading password
        password = driver.find_element(By.XPATH, "//input[@type='password']")
        decode_password = base64.b64decode(encoded_password).decode("utf-8")
        password.send_keys(decode_password)
        next = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
        next.click()
        time.sleep(5)

        title=driver.title
        print(title)
        if title=="Dashboard":
            print("Login Successful")
        else:
            print("Login Unsuccessful")

c1=ClickandSendkey()
c1.login()


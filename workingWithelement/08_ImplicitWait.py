'''
wait for certain amount of time before throwing error
'''

import time

from selenium.webdriver.common.by import By
from seleniumwire import webdriver


class ImplicitWait():
    def implicitwait(self):
        url="https://www.letskodeit.com/home"
        driver=webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,'//a[contains(text(),"Sign")]').click()

        emailField=driver.find_element(By.NAME,"email")
        emailField.send_keys("binayks")

        driver.find_element(By.ID,"login").click()

temp=ImplicitWait()
temp.implicitwait()


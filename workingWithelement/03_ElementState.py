import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class ElementState():

    def is_enabled(self):
        baseurl = "https://www.letskodeit.com/practice"
        driver=webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()

        #Disabling the element
        disableElement=driver.find_element(By.CSS_SELECTOR,"#disabled-button")
        disableElement.click()

        #Cheking state of the element
        textBox=driver.find_element(By.XPATH,'//input[@id="enabled-example-input"]')
        print(textBox.is_enabled())
        #textBox.send_keys("Hiii")
        time.sleep(2)

        # Enabling the element
        disableElement = driver.find_element(By.CSS_SELECTOR, "#enabled-button")
        disableElement.click()

        # Cheking state of the element
        textBox = driver.find_element(By.XPATH, '//input[@id="enabled-example-input"]')
        state=textBox.is_enabled()
        print(state)
        if state ==True:
            textBox.send_keys("Working fine")
            time.sleep(2)
            print("Sent Successfully")
        else:
            print("Element is not enabled")

        driver.close()


a=ElementState()
a.is_enabled()




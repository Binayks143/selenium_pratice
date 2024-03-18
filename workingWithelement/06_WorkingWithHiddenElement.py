from selenium.webdriver.common.by import By
from seleniumwire import webdriver


class HiddenElement():
    def hiddenelement(self):

        baseurl="https://www.letskodeit.com/practice"

        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)

        #finding the element is visible or not
        textbox=driver.find_element(By.CSS_SELECTOR,".inputs.displayed-class")
        temp=textbox.is_displayed()  #true if displayed else false
        print("Test Box is Visible?",temp)

        #Disabling the text box
        hidebutton = driver.find_element(By.CSS_SELECTOR, "#hide-textbox")
        hidebutton.click()

        # finding the element is visible or not
        textbox = driver.find_element(By.CSS_SELECTOR, ".inputs.displayed-class")
        temp = textbox.is_displayed()  # true if displayed else false
        print("Test Box is Visible?", temp)

        # Enabling the text box
        showbutton = driver.find_element(By.XPATH, '//input[@id="show-textbox"]')
        showbutton.click()


        # finding the element is visible or not
        textbox = driver.find_element(By.CSS_SELECTOR, ".inputs.displayed-class")
        temp = textbox.is_displayed()  # true if displayed else false
        print("Test Box is Visible?", temp)




ff=HiddenElement()
ff.hiddenelement()
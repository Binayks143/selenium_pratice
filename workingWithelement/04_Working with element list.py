from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElement():
    baseurl = "https://www.letskodeit.com/practice"
    driver = webdriver.Chrome()
    driver.get(baseurl)
    driver.maximize_window()
    def test_radio_element(self):
        radiobuttonlist=WorkingWithElement.driver.find_elements(By.XPATH,"//input[contains(@type,'radio') and contains(@name,'cars')]")
        size=len(radiobuttonlist)
        print("Total Radio buttons are: ", str(size))
        for i in radiobuttonlist:
            isslected=i.is_selected() #to check the selection
            if not isslected:
                i.click()
                time.sleep(2)

    def checkboxselection(self):
        checkboxlist=WorkingWithElement.driver.find_elements(By.XPATH,'//input[@type="checkbox" and @name="cars"]')
        size=len(checkboxlist)
        print("Total Check boxes is :", size)
        for i in checkboxlist:
            i.click()
            time.sleep(2)




a=WorkingWithElement()
a.test_radio_element()
a.checkboxselection()

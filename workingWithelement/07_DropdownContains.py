#Get all the text form the dorpdown manu
#.text will give text of the element

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from seleniumwire import webdriver

class DropdownContains():

    def dropdowntext(self):
        driver=webdriver.Chrome()
        driver.get("https://www.letskodeit.com/practice")
        driver.maximize_window()

        #finding the dorpdown element on DOM

        dorpdown=driver.find_element(By.ID,"carselect")
        sel=Select(dorpdown)

        #Get all option from dropdown
        option=sel.options

        print("DropDown Options:")
        for i in option:
            print(i.text)

        driver.close()

tt=DropdownContains()
tt.dropdowntext()






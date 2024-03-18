#To select the element in dropdown we have use select class
#every dopdown shouldnot be select class

from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class DropdownSelect():
    def test_select(self):
        baseUrl="https://www.letskodeit.com/practice"
        driver=webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)

        #Finding the dropdone element
        element=driver.find_element(By.ID,"carselect")

        #using Select we are indicating element this is dropdown
        sel=Select(element)

        #we can select the element in many ways like by value,index and visible text.

        sel.select_by_value("benz")
        time.sleep(2)
        print("Select Benz by value")

        sel.select_by_index(0)
        time.sleep(2)
        print("Select BMW by index")

        sel.select_by_visible_text("Honda")
        time.sleep(2)
        print("Select Honda by visible text")
        # Finding the dropdown element
        element = driver.find_elements(By.XPATH, "//select[@id='carselect']/option")
        t1=[]
        for i in element:
            print(i.text)
        #     t1.append(i.text)
        # print("Available dropdown options are: ",t1)


c1=DropdownSelect()
c1.test_select()





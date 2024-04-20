from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")

links=driver.find_elements(By.TAG_NAME,"a")
time.sleep(10)

for i in links:
    link_url=i.get_attribute("href")
    #It retrieves the value of the specified attribute (href in this case) from the element.
    if link_url:
        # Send an HTTP GET request to the link URL
        response=requests.get(link_url)
        # Check if the response status code indicates a broken link
        if response.status_code>=400:
            print("Broken Link Found : "+ link_url)
driver.quit()



driver.quit()
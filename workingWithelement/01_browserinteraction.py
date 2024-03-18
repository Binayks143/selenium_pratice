import time

from selenium import webdriver
class BrowserInteractions():
    def test(self):
        baseurl="https://www.letskodeit.com/practice"
        driver=webdriver.Chrome()

        #maximize window
        driver.maximize_window()

        #Open Base Url
        driver.get(baseurl)

        #Get Tilte of the page
        title=driver.title
        print("Title =", title)

        #Current Url
        curl=driver.current_url
        print("Current URL is "+curl)

        #Broser Refresh
        driver.refresh()

        print("Browser Refresh first time")

        driver.get(driver.current_url)
        print("Browser Refresh second time")

        # open another URL
        driver.get("https://www.letskodeit.com/support")

        print("Another URL"+driver.current_url)

        # Browser back
        driver.back()
        print("Go one step back in browser history")
        time.sleep(2)

        # Browser Forward
        driver.forward()
        print("Go one step forward in browser history")
        time.sleep(2)

        #Get page source
        pageSource=driver.page_source
        #print(pageSource)

        #browser close
        driver.close()


a=BrowserInteractions()
a.test()



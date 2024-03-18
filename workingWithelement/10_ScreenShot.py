from seleniumwire import webdriver


class ScreenShot():
    def takeScreenShot(self):

        driver =webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.letskodeit.com/practice")

        destination_file_path="C:\\Users\\Desktop\\test.png"
        try:
            driver.save_screenshot(destination_file_path)
            print("ScreenShot saved successfully")

        except NotADirectoryError:
            print("Not a direcotory issue")

        driver.close()

ff=ScreenShot()
ff.takeScreenShot()
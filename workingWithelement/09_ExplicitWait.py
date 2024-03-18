from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire import webdriver


class ExplicitWait():
    def Explicitwait(self):
        url="https://www.letskodeit.com/"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)

        driver.find_element(By.XPATH,'//a[contains(text(),"Sign")]').click()

        ExpWait=WebDriverWait(driver,timeout=30,poll_frequency=2,
                              ignored_exceptions=[NoSuchElementException,
                                                  NotImplementedError,
                                                  ElementNotVisibleException])

        element=ExpWait.until(EC.visibility_of_element_located((By.NAME,"email")))
        element.send_keys("test123")
        driver.close()
        

temp=ExplicitWait()
temp.Explicitwait()

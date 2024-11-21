import logging
import traceback
from traceback import print_stack
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from callhub.custom_logger import customLogger


class SeleniumDriver:
    log = customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        title = self.driver.title
        self.log.info(f"Current Page Title is '{title}'")
        return title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "linktext":
            return By.LINK_TEXT
        elif locatorType == "partiallinktext":
            return By.PARTIAL_LINK_TEXT
        elif locatorType == "tagname":
            return By.TAG_NAME
        else:
            self.log.info(f"'{locatorType}' is not a Valid Locator")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        """
        Get list of elements
        """
        elements = []
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elements = self.driver.find_elements(byType, locator)
            if len(elements) > 0:
                self.log.info(f"Element list found with locator: {locator} and locatorType: {locatorType}. Number of "
                              f"elements found: {len(elements)}")
            else:
                self.log.warning(f"Element list not found with locator: {locator} and locatorType: {locatorType}.")

        except NoSuchElementException:
            self.log.error(f"Element list not found with locator: {locator} and locatorType: {locatorType}")
        except Exception as e:
            self.log.error(f"An unexpected error occurred: {str(e)}")
        return elements

    def elementClick(self, locator="", locatorType="id", element=None):
        """
        Click on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                # element = self.getElement(locator, locatorType)
                element = self.waitForElement(locator, locatorType, timeout=5, pollFrequency=0.5)
                element.click()
                self.log.info("Clicked on element with locator: " + locator +
                              " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        """
        Send keys to an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info(f"Sent data={data} on element with locator: {locator} and locatorType: {locatorType}")
        except:
            self.log.info(f"Cannot send data={data} on the element with locator: {locator} "
                          f"and locatorType: {locatorType}")
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))

    def isElementPresent(self, locator="", locatorType="id", element=None):
        element_list = []
        try:
            if locator:
                element_list = self.getElementList(locator, locatorType)
            elif element:  # Direct element is provided
                element_list = [element]

            if element_list:
                self.log.info(f"Element present with locator: {locator}, locatorType: {locatorType}")
                return True
            else:
                self.log.warning(f"Element not present with locator: {locator}, locatorType: {locatorType}")
                return False
        except Exception as e:
            self.log.error(f"Error occurred while checking for element presence: {str(e)}")
            return False

    def waitForElement(self, locator, locatorType="id",
                       timeout=5, pollFrequency=1):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info(f"waiting for maximum {timeout} second for element to clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException, NoSuchFrameException,
                                                     StaleElementReferenceException, TimeoutException,
                                                     ElementClickInterceptedException, InvalidElementStateException,
                                                     NoSuchWindowException, JavascriptException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element Appeared on the webpage")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def selectDropdownOption(self, locator="", locatorType="id", option="value", optionData=""):

        try:
            if locator:  # This means if locator is not empty
                element = self.waitForElement(locator, locatorType)
                element.click()
                self.log.info("Clicked on the dropdown element with locator: " + locator +
                              " and locatorType: " + locatorType)
                sel = Select(element)
                if option == "visibleText":
                    sel.select_by_visible_text(optionData)
                    self.log.info(f"Selected dropdown option with given visible_text='{optionData}'")
                elif option == "index":
                    sel.select_by_index(int(optionData))
                    self.log.info(f"Selected dropdown option with given index='{optionData}'")

                elif option == "value":
                    sel.select_by_value(optionData)
                    self.log.info(f"Selected dropdown option with given value='{optionData}'")

        except:
            self.log.error("Cannot click on dropdown element the element with locator: " + locator +
                           " locatorType: " + locatorType)
            print_stack()

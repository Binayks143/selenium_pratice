from traceback import print_stack
import logging
import custom_logger as cl
from callhub.selenium_base_class import SeleniumDriver


class HelpertestStatus(SeleniumDriver):
    log = cl.customLogger(logging.INFO)
    resultList = []  # Class variable to keep track of all the results

    def initialize(self, driver):
        """
        Initialize the Helper testStatus class
        Initialize the Helper testStatus class
        """
        self.driver = driver
        self.resultList = []  # Clear result list for each initialization

    def setResult(self, testName="Failed_TC", result=None, resultMessage=None):
        """
        Set the result of a verification point
        """
        try:
            if result is not None:
                if result:
                    self.resultList.append('PASS')
                    self.log.info("### VERIFICATION SUCCESSFUL : " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :" + resultMessage + "=FALSE")
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :" + resultMessage + "=FALSE")
        except Exception as e:
            self.resultList.append("FAIL")
            self.log.error("### Some exception occurred" + str(e))
            print_stack()

    def mark(self, result, resultMessage):
        """
        Mark the result of a single verification point in a test case.
        """
        self.setResult(result=result, resultMessage=resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of a test case based on multiple verification points.
        If any verification fails, the test case fails.
        """
        self.setResult(testName, result, resultMessage)
        if "FAIL" in self.resultList:
            self.log.error(testName + " Test case Failed !!!!")
            self.resultList.clear()
            assert False, f"{testName} Test case failed. Check logs for details."
            # intentionally failing the test case because if any one test case will fail all
            # test case will be failed.
        else:
            self.log.info(testName + " Test Case Passed")
            self.resultList.clear()
            assert True

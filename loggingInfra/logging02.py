import logging
import loggingInfra.custom_logger as cl

class Logging02():
    log=cl.customlogger(logging.DEBUG)

    def method1(self):
        self.log.debug("This is Debug message")
        self.log.info("This is INFO message")
        self.log.warning("This is WARNING message")
        self.log.error("This is ERROR message")
        self.log.critical("This is Critical message")

    def method2(self):
        self.log.debug("This is Debug message")
        self.log.info("This is INFO message")
        self.log.warning("This is WARNING message")
        self.log.error("This is ERROR message")
        self.log.critical("This is Critical message")

    def method3(self):
        m3log=cl.customlogger(logging.INFO)
        m3log.debug("This is debug message")
        m3log.info("This is info message")
        m3log.warning("This is warning message")
        m3log.error("This is error message")
        m3log.critical("This is critical message")

demo=Logging02()
demo.method1()
demo.method2()
demo.method3()



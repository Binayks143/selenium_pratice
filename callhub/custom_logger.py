import inspect
import logging


def customLogger(logLevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]

    logger = logging.getLogger(loggerName)
    # By default, log all messages

    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler(r"C:\Binay\PyChamp\selenium_pratice\callhub\automation.log",
                                      mode='a', encoding='utf-8')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%d/%m/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger

import inspect
import logging

def customlogger(loglevel):
    # Gets the name of the class / method from where this method is called
    loggerName=inspect.stack()[1][3]
    logger=logging.getLogger(loggerName)

    #By default all logs will be displayed
    logger.setLevel(logging.DEBUG)

    fileHandler=logging.FileHandler(f"{loggerName}.log",mode='w')
    fileHandler.setLevel(loglevel)

    formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger


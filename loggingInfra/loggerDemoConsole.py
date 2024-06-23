"""
Logging infrastructure in Python typically involves using the built-in logging module,
which provides a flexible framework for logging messages from your Python programs.
Here's a basic outline of how you can set up logging infrastructure in Python:

Logger- it looks the message and it will create a log message objeect from message string
once it will create a object it will pass it to handler

Create a logger named 'example_logger'.
Set the logging level of the logger to DEBUG.
Create a FileHandler named file_handler to write log messages to a file.
Set the logging level of the file handler to DEBUG.
Create a formatter specifying the desired format for log messages.
Add the formatter to the file handler.
Add the file handler to the logger.
Log messages of various levels using the logger.
"""

import logging

class LoggerDemoConsole():

    def testlog(self):
        # Create a Logger
        #logger name : LoggerDemoConsole.__name__ , here we can give any name but better to give class name
        #so that we can get to know from where this log is coming.

        logger=logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        #Create a console Handler and set the level to INFO
        file_handler=logging.StreamHandler()
        file_handler.setLevel(logging.INFO)

        #Create a Formatter
        #%(name)s for file name given at getLogger
        formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s",
                    datefmt="%d/%m/%Y %I:%M:%S %p")

        # Add formatter to handler
        file_handler.setFormatter(formatter)

        # Add handler to logger
        logger.addHandler(file_handler)

        # Log messages
        logger.debug('Debug message')
        logger.info('Info message')
        logger.warning('Warning message')
        logger.error('Error message')
        logger.critical('Critical message')


o1=LoggerDemoConsole()
o1.testlog()



import logging
import logging.config

class LoggerDemoConf():
    def testlog(self):
        #create a logger
        logging.config.fileConfig("logging.conf")
        logger=logging.getLogger(LoggerDemoConf.__name__)

        # Log messages
        logger.debug('Debug message')
        logger.info('Info message')
        logger.warning('Warning message')
        logger.error('Error message')
        logger.critical('Critical message')

demo=LoggerDemoConf()
demo.testlog()



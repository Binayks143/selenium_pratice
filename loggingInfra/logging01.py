"""
Logging Levels
1. DEBUG: Detailed information, typically of interest only when diagnosing problems.
2. INFO: Confirmation that things are working as expected.
3. WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g., ‘disk space low’). The software is still functioning as expected.
4. ERROR: Due to a more serious problem, the software has not been able to perform some function.
5. CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
"""

"""
Logging Format  details info
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#time.strftime
"""

import logging

logging.basicConfig(filename="test.log",level=logging.DEBUG,filemode='a',
                    format="%(asctime)s - %(levelname)s: %(message)s",
                    datefmt="%d/%m/%Y %I:%M:%S %p")
logging.debug("This DEBUG message")
logging.warning("This is Warning message")
logging.info("This is info message")
logging.error("This is ERROR message")


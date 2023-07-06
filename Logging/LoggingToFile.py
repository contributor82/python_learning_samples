
# Logging to file

import logging
import logging.config as logConfig

class LoggingToFile: 

    def config_logging(self): 
        try:
            logging.basicConfig(filename='Data\\datalog.log', filemode='a', encoding='UTF-8', level=logging.DEBUG)
        except Exception as ex:
            raise(FileNotFoundError)

    def logging_to_file(self): 
        try: 
            logging.debug("logging:debug - This message should be logged in log file. ")
            logging.info("logging:info - This message should be logged in log file. ")
            logging.warning("logging:warning - This messagen should be logged in log file. ")
            logging.error("non-ASCII stuff, too, like Øresund and Malmö")

        except Exception as ex: 
            print(ex)
    
    def get_current_logging_level(self): 
        try: 
            logger = logging.getLogger(__name__)
            effectiveLevel = logger.getEffectiveLevel()
            levelName = logging.getLevelName(effectiveLevel)
            print("Current Logging level configured: ", levelName)
        except Exception as ex:
            print(ex)

    
logger = LoggingToFile()
logger.config_logging()
logger.logging_to_file()
logger.get_current_logging_level()






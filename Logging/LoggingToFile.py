
# Logging to file

import logging


class LoggingToFile: 

    def config_logging(self, logFile: str) -> None: 
        try:
            logging.basicConfig(filename=logFile, filemode='a', encoding='UTF-8', level=logging.DEBUG)
        except FileNotFoundError as ex:
            raise(ex)

    def logging_to_file(self) -> None: 
        try: 
            logging.debug("logging:debug - This message should be logged in log file. ")
            logging.info("logging:info - This message should be logged in log file. ")
            logging.warning("logging:warning - This messagen should be logged in log file. ")
            logging.error("non-ASCII stuff, too, like Øresund and Malmö")

        except Exception as ex: 
            print(ex)
    
    def get_current_logging_level(self) -> None: 
        try: 
            logger = logging.getLogger(__name__)
            effectiveLevel = logger.getEffectiveLevel()
            levelName = logging.getLevelName(effectiveLevel)
            print("Current Logging level configured: ", levelName)
        except Exception as ex:
            print(ex)

if __name__ == '__main__':
    logger = LoggingToFile()
    logger.config_logging('C:\\Data\\datalog.log')
    logger.logging_to_file()
    logger.get_current_logging_level()






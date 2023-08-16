"""Module to log to file """
import logging

class LoggingToFile:
    """Logging to file class """

    def config_logging(self, log_file: str) -> None:
        """Configure logging method """
        try:
            logging.basicConfig(filename=log_file, filemode='a',
                                encoding='UTF-8', level=logging.DEBUG)
        except FileNotFoundError as file_not_found_error:
            print(file_not_found_error)
        except FileExistsError as file_exists_error:
            print(file_exists_error)

    def logging_to_file(self) -> None:
        """Logging to file method """
        try:
            logging.debug("logging:debug - This message should be logged in log file. ")
            logging.info("logging:info - This message should be logged in log file. ")
            logging.warning("logging:warning - This messagen should be logged in log file. ")
            logging.error("non-ASCII stuff, too, like Øresund and Malmö")

        except RuntimeError as log_to_file_run_time_error:
            print(log_to_file_run_time_error)

    def get_current_logging_level(self) -> None:
        """Get current logging level method """
        try:
            logger: logging.Logger = logging.getLogger(__name__)
            effective_level: int = logger.getEffectiveLevel()
            level_name: str = logging.getLevelName(effective_level)
            print("Current Logging level configured: ", level_name)
        except RuntimeError as run_time_error:
            print(run_time_error)

if __name__ == '__main__':
    log_to_file = LoggingToFile()
    log_file_name: str = 'C:\\Data\\datalog.log'
    log_to_file.config_logging(log_file_name)
    log_to_file.logging_to_file()
    log_to_file.get_current_logging_level()

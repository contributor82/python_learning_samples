"""Module for Logging from threads """
import logging
import threading
import time


class LogginFromThreads:
    """Logging from threads class """

    def config_logging(self, log_file: str) -> None:
        """ configuring logging to log in file """
        try:
            logging.basicConfig(filename=log_file, filemode='a',
                                encoding='UTF-8', level=logging.DEBUG,
                                format='%(relativeCreated)6d,→%(threadName)s %(message)s')
        except FileNotFoundError as file_not_found_error:
            print(file_not_found_error)
        except FileExistsError as file_exists_error:
            print(file_exists_error)

    def worker_thread(self, args: dict[str,bool]) -> None:
        """ Logging from worker thread """
        try:
            while not args['stop']:
                logging.debug('Hi, I am from worker thread. ')
                time.sleep(0.5)
        except threading.ThreadError as thread_error:
            print(thread_error)


    def main_thread(self) -> None:
        """ Logging from main thread """

        self.config_logging('C:\\Data\\logging_from_threads.log')
        info: dict[str,bool] = {'stop': False}
        thread = threading.Thread(target=self.worker_thread, args=(info, ))
        thread.start()

        while True:
            try:
                logging.debug("Hi, I am from main thread. ")
                time.sleep(0.75)
            except KeyboardInterrupt as key_board_interrupt_ex:
                info['stop']= True
                print(key_board_interrupt_ex)
                break
        thread.join()

if __name__ == '__main__':
    threads_logging_instance = LogginFromThreads()
    threads_logging_instance.main_thread()

import logging
import threading
import time


class LogginFromThreads: 

    def config_logging(self, log_file: str) -> None: 
        ### configuring logging to log in file ###
        try:
            logging.basicConfig(filename=log_file, filemode='a', encoding='UTF-8', level=logging.DEBUG, 
                                format='%(relativeCreated)6d,→%(threadName)s %(message)s')
        except FileNotFoundError as ex:
            raise(ex)

    def worker_thread(self, args: any): 
        ### Logging from worker thread ###
        try: 
            while not args['stop']: 
                logging.debug('Hi, I am from worker thread. ')
                time.sleep(0.5)
        except Exception as ex: 
            print(ex)


    def main_thread(self): 
        ### Logging from main thread ###

        self.config_logging('C:\\Data\\logging_from_threads.log')
        info = {'stop': False}
        thread = threading.Thread(target=self.worker_thread, args=(info, )) 
        thread.start()

        while True: 
            try: 
                logging.debug("Hi, I am from main thread. ")
                time.sleep(0.75)
            except KeyboardInterrupt as ki:
                info['stop']= True
                print(ki)
                break
        thread.join()          

if __name__ == '__main__': 
    
    threads_logging_instance = LogginFromThreads()
    threads_logging_instance.main_thread()
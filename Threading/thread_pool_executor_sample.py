
# Using concurrent.futures, performing asynchronous execution of callables. 
# When max Worker value is not given, it will default to number of processor from the machine. 
# if max worker value is given, it will use the number of threads to execute the task.
# ThreadPoolExecutor often used to overlap I/O instead of CPU work.
# It uses idle worker thread before using maxWorker worker threads. 
# Avoid using this for long running task.
# Exception in main thread must be caught to signal threads to exit out gracefully. 

import concurrent.futures
import urllib.request

class ThreadPoolExecutorSample: 

    # Taken URLs are from Python documentation
    urls = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/']

    # Opening url and reading bytes. 
    def load_url(self, url : str, timeout : float | None) -> object: 
        try: 
            with urllib.request.urlopen(url, timeout=timeout) as conn: 
                 return conn.read()
        except Exception as ex:
            print(ex)
    # Using ThreadPoolExecutor as executor to process the call 
    def execute_async(self, max_workers : int | None) -> None: 
        data_from_url : object
        try: 
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor: 
                url_collection = { executor.submit(self.load_url, url, 60): url for url in self.urls }
                for future in concurrent.futures.as_completed(url_collection): 
                    url = url_collection[future]
                    try:
                        data_from_url = future.result()
                    except Exception as exc:
                        print('%r generated an exception: %s' % (url, exc))
                    else:
                        print('%r page is %d bytes' % (url, len(data_from_url)))
        except Exception as ex: 
            print(ex)

if __name__ == '__main__':
    async_exec_instance = ThreadPoolExecutorSample()
    async_exec_instance.execute_async(5)

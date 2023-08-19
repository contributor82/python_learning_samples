"""Module for thread pool executor sample """
# Using concurrent.futures, performing asynchronous execution of callables.
# When max Worker value is not given, it will default to number of processor from the machine.
# if max worker value is given, it will use the number of threads to execute the task.
# ThreadPoolExecutor often used to overlap I/O instead of CPU work.
# It uses idle worker thread before using maxWorker worker threads.
# Avoid using this for long running task.
# Exception in main thread must be caught to signal threads to exit out gracefully.
import concurrent.futures
from urllib.error import URLError
import urllib.request

class ThreadPoolExecutorSample:
    """Thread pool executor sample class """
    # Taken URLs are from Python documentation
    urls: list[str] = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/']


    def load_url(self, url : str, timeout : float | None) -> object:
        """ Load url method for opening url and reading bytes. """
        url_data: object | None
        try:
            with urllib.request.urlopen(url, timeout = timeout) as conn:
                url_data = conn.read()
        except URLError as ex:
            print(ex)
            url_data = None
        return url_data

    def execute_async(self, max_workers : int | None) -> None:
        """Execute async """
        # Using ThreadPoolExecutor as executor to process the call
        data_from_url : object
        url: str = ''
        try:

            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                url_collection: dict[concurrent.futures.Future[object | None], str] = {
                    executor.submit(self.load_url, url, 60):
                    url for url in self.urls }
                for completed_future in concurrent.futures.as_completed(url_collection):
                    url = url_collection[completed_future]
                    try:
                        data_from_url = completed_future.result()
                    except concurrent.futures.CancelledError as cancelled_error:
                        print(cancelled_error)
                    except concurrent.futures.TimeoutError as time_out_error:
                        print(f'{url!r} generated an exception {time_out_error.args[0]!r}')
                        # print('%r generated an exception: %s" % (url, exc))
                    else:
                        print(f'{url!r} page is { len(str(data_from_url)) } bytes')
                        # print('%r page is %d bytes' % (url, len(str(data_from_url))))
        except RuntimeError as run_time_error:
            print(run_time_error)

if __name__ == '__main__':
    async_exec_instance = ThreadPoolExecutorSample()
    async_exec_instance.execute_async(5)

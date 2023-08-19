
"""Module for threading using queue """
# Controlling over dispatching algorithm
# Adding list of jobs in queue
# Pulling jobs from queue and executing them
# Achieveing this functionality using threading and queue

import threading
import queue
import time

class ThreadingUsingQueue:
    """Threading using queue """
    thread_queue: queue.Queue[str]

    def __init__(self, max_size: int) -> None:
        """Initializing thread using queue """
        self.thread_queue = queue.Queue(max_size)

    def pulling_job_from_queue(self) -> None:
        """Pulling job from queue method """
        print('Running worker ')
        time.sleep(0.1)
        item: int
        while True:
            try:
                item = self.thread_queue.get(False) # type: ignore

            except queue.Empty:
                print('Worker', threading.current_thread(), ' ')
                print('Queue empty')
                break
            else:
                print('Worker', threading.current_thread(), ' ', 'Running with argument ', item)
                time.sleep(0.5)


    def adding_job_in_queue(self, job_range_val : int) -> None:
        """Adding job in queue method """
        for job in range(job_range_val):
            job_item: str = str(job)
            self.thread_queue.put(job_item)

    def starting_worker_pool(self, worker_range_val: int) -> None:
        """Starting worker pool method """
        for i in range(worker_range_val):
            thread_name: str = f'Worker {(i+1)}'
            thread = threading.Thread(target=self.pulling_job_from_queue, name=thread_name)
            thread.start()

if __name__ == '__main__':
    tuq_instance = ThreadingUsingQueue(0)
    tuq_instance.adding_job_in_queue(50)
    tuq_instance.starting_worker_pool(2)
    print('Main thread sleeping')
    time.sleep(5)

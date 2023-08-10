
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

    thread_using_que = queue.Queue(0)

    def pulling_job_from_queue(self) -> None:
        """Pulling job from queue method """
        print("Running worker ")
        time.sleep(0.1)
        while True:
            try:
                arg: object = self.thread_using_que.get(block=False)

            except queue.Empty:
                print('Worker', threading.current_thread(), ' ')
                print('Queue empty')
                break
            else:
                print('Worker', threading.current_thread(), ' ', 'Running with argument ', arg)
                time.sleep(0.5)


    def adding_job_in_queue(self, job_range_val : int) -> None:
        """Adding job in queue method """
        for i in range(job_range_val):
            self.thread_using_que.put(i)

    def starting_worker_pool(self, worker_range_val: int) -> None:
        """Starting worker pool method """
        for i in range(worker_range_val):
            thread = threading.Thread(target=self.pulling_job_from_queue, name='Worker %i' % (i+1))
            thread.start()

if __name__ == '__main__':
    tuq_instance = ThreadingUsingQueue()
    tuq_instance.adding_job_in_queue(50)
    tuq_instance.starting_worker_pool(2)
    print('Main thread sleeping')
    time.sleep(5)

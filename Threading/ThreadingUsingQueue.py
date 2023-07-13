
# Controlling over dispatching algorithm
# Adding list of jobs in queue
# Pulling jobs from queue and executing them
# Achieveing this functionality using threading and queue

import threading, queue, time

class ThreadingUsingQueue: 
    q = queue.Queue()

    def pulling_job_from_queue(self):
        print("Running worker ")
        time.sleep(0.1)
        while True: 
            try: 
                arg = self.q.get(block=False)

            except queue.Empty: 
                print('Worker', threading.current_thread(), ' ') 
                print('Queue empty')
                break
            else: 
                print('Worker', threading.current_thread(), ' ', 'Running with argument ', arg)
                time.sleep(0.5)


    def adding_job_in_queue(self, jobRange): 
        for i in range(jobRange): 
            self.q.put(i)

    def starting_worker_pull(self, workerRange): 
        for i in range(workerRange): 
            t = threading.Thread(target=self.pulling_job_from_queue, name='Worker %i' % (i+1))
            t.start()

if __name__ == '__main__': 
    tuqInstance = ThreadingUsingQueue()
    tuqInstance.adding_job_in_queue(50)
    tuqInstance.starting_worker_pull(2)
    print('Main thread sleeping')
    time.sleep(5)

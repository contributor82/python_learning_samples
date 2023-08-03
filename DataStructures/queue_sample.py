import queue

class QueueSample: 
    fifoQueue: queue.Queue[str]
    lifoQueue: queue.LifoQueue[str]
    priorityQueue: queue.PriorityQueue[str]
    simpleQueue: queue.SimpleQueue[str]

    def init_queue(self, maxSize: int) -> None: 
        self.fifoQueue = queue.Queue(maxSize)
        self.lifoQueue = queue.LifoQueue(maxSize)
        self.priorityQueue = queue.PriorityQueue(maxSize)
        self.simpleQueue = queue.SimpleQueue()

    def append_fifo_queue(self, element: str) -> None: 
        self.fifoQueue.put(element)

    def append_lifo_queue(self, element: str) -> None: 
        self.lifoQueue.put(element)

    def append_priority_queue(self, element: str) -> None: 
        self.priorityQueue.put(element)
    
    def append_simple_queue(self, element: str) -> None: 
        self.simpleQueue.put(element)
    
    def display_fifo_queue(self) -> None: 
        try: 
            while True:
                item = self.fifoQueue.get(False)
                print(f'Working on FIFO Queue item {item}')
                print(f'Finished on FIFO Queue item {item}')
                self.fifoQueue.task_done()
        except Exception as ex: 
            print(ex)


    def display_lifo_queue(self) -> None: 
        try: 
            while True:
                item = self.lifoQueue.get(False)
                print(f'Working on LIFO Queue item {item}')
                print(f'Finished on LIFO Queue item {item}')
                self.lifoQueue.task_done()
        except Exception as ex: 
            print(ex)
    
    def display_priority_queue(self) -> None: 
        try: 
            while True:
                item = self.priorityQueue.get(False)
                print(f'Working on Priority Queue item {item}')
                print(f'Finished on Priority Queue item {item}')
                self.priorityQueue.task_done()
        except Exception as ex: 
            print(ex)
    
    def display_simple_queue(self) -> None: 
        try: 
            while True:
                item = self.simpleQueue.get(False)
                print(f'Working on Simple Queue item {item}')
                print(f'Finished on Simple Queue item {item}')
                if self.simpleQueue.empty() == True: break
        except Exception as ex: 
            print(ex)

    def get_fifo_queue_element(self)-> str:
        try:
            item = self.fifoQueue.get(False)
            return item
        except Exception as ex: 
            print(ex)
            return ""

    def get_lifo_queue_element(self) -> str: 
        try:
            item = self.lifoQueue.get(False)
            return item
        except Exception as ex: 
            print(ex)
            return ""
    
    def get_priority_queue_element(self) -> str: 
        try: 
            item = self.priorityQueue.get(False)
            return item
        except Exception as ex: 
            print(ex)
            return ""

    def get_simple_queue_element(self) -> str: 
        try: 
            item = self.simpleQueue.get(False)
            return item
        except Exception as ex: 
            print(ex)
            return ""
    
    def get_simple_queue_size(self) -> int: 
        return self.simpleQueue.qsize()

if __name__ == '__main__': 
    qs_instance =  QueueSample()
    qs_instance.init_queue(10)

    qs_instance.append_fifo_queue("Fifo Element 1")
    qs_instance.append_fifo_queue("Fifo Element 2")
    qs_instance.append_fifo_queue("Fifo Element 3")
    qs_instance.append_fifo_queue("Fifo Element 4")


    qs_instance.append_lifo_queue("Lifo Element 1")
    qs_instance.append_lifo_queue("Lifo Element 2")
    qs_instance.append_lifo_queue("Lifo Element 3")
    qs_instance.append_lifo_queue("Lifo Element 4")

    qs_instance.append_priority_queue("Priority Element 1")
    qs_instance.append_priority_queue("Priority Element 2")
    qs_instance.append_priority_queue("Priority Element 3")
    qs_instance.append_priority_queue("Priority Element 4")

    qs_instance.append_simple_queue("Simple Element 1")
    qs_instance.append_simple_queue("Simple Element 2")
    qs_instance.append_simple_queue("Simple Element 3")
    qs_instance.append_simple_queue("Simple Element 4")

    print(" fifo queue element: ", qs_instance.get_fifo_queue_element())
    print(" lifo queue element: ", qs_instance.get_lifo_queue_element())
    print(" priority queue element: ", qs_instance.get_priority_queue_element())
    print(" simple queue element: ", qs_instance.get_simple_queue_element())
    print(" simple queue size: ", qs_instance.get_simple_queue_size())
    

    qs_instance.display_fifo_queue()
    qs_instance.display_lifo_queue()
    qs_instance.display_priority_queue()
    qs_instance.display_simple_queue()

    
    


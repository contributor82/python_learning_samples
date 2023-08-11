"""Module for Queue sample """
import queue

class QueueSample:
    """ Queue sample class """
    fifo_queue: queue.Queue[str]
    lifo_queue: queue.LifoQueue[str]
    priority_queue: queue.PriorityQueue[str]
    simple_queue: queue.SimpleQueue[str]

    def init_queue(self, max_size: int) -> None:
        """ Initialize queue """
        self.fifo_queue = queue.Queue(max_size)
        self.lifo_queue = queue.LifoQueue(max_size)
        self.priority_queue = queue.PriorityQueue(max_size)
        self.simple_queue = queue.SimpleQueue()

    def append_fifo_queue(self, element: str) -> None:
        """ Append fifo queue method """
        self.fifo_queue.put(element)

    def append_lifo_queue(self, element: str) -> None:
        """ Append lifo queue """
        self.lifo_queue.put(element)

    def append_priority_queue(self, element: str) -> None:
        """ Append priority queue """
        self.priority_queue.put(element)

    def append_simple_queue(self, element: str) -> None:
        """ Append simple queue """
        self.simple_queue.put(element)

    def display_fifo_queue(self) -> None:
        """ Display fifo queue """
        item: str = ""
        try:
            while True:
                item = self.fifo_queue.get(False)
                print(f'Working on FIFO Queue item {item}')
                print(f'Finished on FIFO Queue item {item}')
                self.fifo_queue.task_done()
        except queue.Empty as queue_empty:
            print(queue_empty)

    def display_lifo_queue(self) -> None:
        """ Display lifo queue """
        item: str = ""
        try:
            while True:
                item = self.lifo_queue.get(False)
                print(f'Working on LIFO Queue item {item}')
                print(f'Finished on LIFO Queue item {item}')
                self.lifo_queue.task_done()
        except queue.Empty as queue_empty:
            print(queue_empty)

    def display_priority_queue(self) -> None:
        """ Display priority queue """
        item: str = ""
        try:
            while True:
                item = self.priority_queue.get(False)
                print(f'Working on Priority Queue item {item}')
                print(f'Finished on Priority Queue item {item}')
                self.priority_queue.task_done()
        except queue.Empty as queue_empty:
            print(queue_empty)

    def display_simple_queue(self) -> None:
        """ Display simple queue """
        item: str = ""
        try:
            while True:
                item = self.simple_queue.get(False)
                print(f'Working on Simple Queue item {item}')
                print(f'Finished on Simple Queue item {item}')
                if self.simple_queue.empty() is True:
                    break
        except queue.Empty as queue_empty:
            print(queue_empty)

    def get_fifo_queue_element(self) -> str:
        """ Get fifo queue element """
        item: str = ""
        try:
            item = self.fifo_queue.get(False)
        except queue.Empty as queue_empty:
            print(queue_empty)
        return item

    def get_lifo_queue_element(self) -> str:
        """ Get lifo queue element """
        item: str = ""
        try:
            item = self.lifo_queue.get(False)
        except queue.Empty as queue_empty:
            print(queue_empty)
        return item

    def get_priority_queue_element(self) -> str:
        """ Get priority queue element """
        item: str = ""
        try:
            item = self.priority_queue.get(False)
            return item
        except queue.Empty as queue_empty:
            print(queue_empty)
        return item

    def get_simple_queue_element(self) -> str:
        """ Get simple queue element """
        item: str = ""
        try:
            item = self.simple_queue.get(False)
        except queue.Empty as queue_empty:
            print(queue_empty)
        return item

    def get_simple_queue_size(self) -> int:
        """ Get simple queue size """
        return self.simple_queue.qsize()


if __name__ == '__main__':
    qs_instance = QueueSample()
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

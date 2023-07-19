# List as Queue
# Queue - First In, First Out

from collections import deque

# Deque object initialized from left-to-right
# Generalization of stacks & queues
# Thread-safe, double ended, pops from either side of deque
class DequeSample: 
    dq = deque[str]

    def init_deque(self) ->  None: 
        self.dq = deque({"Element 1", "Element 2", "Element 3"})

    def print_deque(self, deque_action: str)-> None: 
        print("Deque Action: ", deque_action, " Deque elements: ", self.dq)

    def append_deque(self, element: str)-> None: 
        self.dq.append(element)    

    def pop_from_right_side(self) -> str: 
        return self.dq.pop()
    
    def  pop_from_left_side(self) -> str: 
        return self.dq.popleft()
    

if __name__ == '__main__': 
    
    dsInstance =  DequeSample()
    dsInstance.init_deque()
    dsInstance.append_deque("Element 4")
    dsInstance.append_deque("Element 5")
    dsInstance.append_deque("Element 6")
    dsInstance.append_deque("Element 7")

    dsInstance.print_deque(" 'Initial' ")

    print("pop from left side: ", dsInstance.pop_from_left_side())

    dsInstance.print_deque(" 'After pop left' ")


    print("pop from right side: ", dsInstance.pop_from_right_side())

    dsInstance.print_deque(" 'After pop' ")

    

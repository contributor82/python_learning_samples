# List as Queue
# Queue - First In, First Out
# Deque object initialized from left-to-right
# Generalization of stacks & queues
# Thread-safe, double ended, pops from either side of deque

from collections import deque

class DequeSample: 
    dq = deque[str]

    def init_deque(self) ->  None: 
        self.dq = deque({"Element 1", "Element 2", "Element 3"})

    def print_deque(self, deque_action: str)-> None: 
        print("Deque Action: ", deque_action, " Deque elements: ", self.dq)

    def append_deque(self, element: str)-> None: 
        self.dq.append(element)     # type: ignore

    def pop_from_right_side(self) -> str: 
        return self.dq.pop() # type: ignore
    
    def  pop_from_left_side(self) -> str: 
        return self.dq.popleft() # type: ignore
    

if __name__ == '__main__': 
    
    ds_Instance =  DequeSample()
    ds_Instance.init_deque()
    ds_Instance.append_deque("Element 4")
    ds_Instance.append_deque("Element 5")
    ds_Instance.append_deque("Element 6")
    ds_Instance.append_deque("Element 7")

    ds_Instance.print_deque(" 'Initial' ")

    print("pop from left side: ", ds_Instance.pop_from_left_side())

    ds_Instance.print_deque(" 'After pop left' ")


    print("pop from right side: ", ds_Instance.pop_from_right_side())

    ds_Instance.print_deque(" 'After pop' ")

    

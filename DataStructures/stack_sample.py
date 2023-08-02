# # Using lists as stack
# Stack - Last In, First Out

class StackSample: 
    stack = None

    def init_stack(self)-> None: 
        self.stack = []

    def append_stack(self, element: int) ->  None: 
        self.stack.append(element)

    def get_stack_element(self) -> int:
        try:  
            item = self.stack.pop()
            return item
        except Exception as ex: 
            print (ex)
            return 0
    
    def display_stack(self): 
        print("Stack: ", self.stack)


if __name__ == '__main__': 
    ssInstance = StackSample()
    ssInstance.init_stack()
    ssInstance.append_stack(1)
    ssInstance.append_stack(2)
    ssInstance.append_stack(3)
    ssInstance.append_stack(4)
    ssInstance.append_stack(5)
    ssInstance.append_stack(6)
    ssInstance.append_stack(7)
    ssInstance.append_stack(8)
    ssInstance.append_stack(9)
    ssInstance.append_stack(10)
    
    ssInstance.display_stack()

    print(" Get element from stack : ", ssInstance.get_stack_element())
    
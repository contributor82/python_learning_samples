# # Using lists as stack
# Stack - Last In, First Out

class StackSample: 
    stack = []

    def init_stack(self)-> None: 
        self.stack = [type(int)]

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
    ss_instance = StackSample()
    ss_instance.init_stack()
    ss_instance.append_stack(1)
    ss_instance.append_stack(2)
    ss_instance.append_stack(3)
    ss_instance.append_stack(4)
    ss_instance.append_stack(5)
    ss_instance.append_stack(6)
    ss_instance.append_stack(7)
    ss_instance.append_stack(8)
    ss_instance.append_stack(9)
    ss_instance.append_stack(10)
    
    ss_instance.display_stack()

    print(" Get element from stack : ", ss_instance.get_stack_element())
    
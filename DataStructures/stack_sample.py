# # Using lists as stack
# Stack - Last In, First Out

class StackSample: 
    stack = []

    def init_stack(self)-> None: 
        ### Initialize stack ###
        self.stack = [type(int)]

    def append_stack(self, element: int) ->  None: 
        ### Append stack ###
        self.stack.append(element)

    def get_stack_element(self) -> int:
        ### Get stack element ###
        item: int =0
        try:  
            item = self.stack.pop()
        except Exception as get_stack_element_ex: 
            print (get_stack_element_ex)
        return item
    
    def display_stack(self) -> None: 
        ### Display stack elements ###
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
    
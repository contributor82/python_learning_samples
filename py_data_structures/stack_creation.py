"""Module for Lists as stack """
# Stack - Last In, First Out

class StackCreation:
    """Stack creation class """
    stack: list[int] = [int] # type: ignore

    #def init_stack(self)-> None:
    #    """ Initialize stack """
    #    self.stack = [int]

    def append_stack(self, element: int) ->  None:
        """ Append stack """
        self.stack.append(element)

    def get_stack_element(self) -> int:
        """ Get stack element """
        item: int =0
        try:
            item = self.stack.pop()
        except UnboundLocalError as unbound_local_error:
            print (unbound_local_error)
        return item

    def display_stack(self) -> None:
        """ Display stack elements """
        print('Stack: ', self.stack)


if __name__ == '__main__':
    sc_instance = StackCreation()
    # sc_instance.init_stack()
    sc_instance.append_stack(1)
    sc_instance.append_stack(2)
    sc_instance.append_stack(3)
    sc_instance.append_stack(4)
    sc_instance.append_stack(5)
    sc_instance.append_stack(6)
    sc_instance.append_stack(7)
    sc_instance.append_stack(8)
    sc_instance.append_stack(9)
    sc_instance.append_stack(10)
    sc_instance.display_stack()

    print(' Get element from stack : ', sc_instance.get_stack_element())

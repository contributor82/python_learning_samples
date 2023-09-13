"""Module for sub decorator two class"""

from base_class import BaseClass
from decorator_class import Decorator

class SubDecoratorTwo(Decorator):
    """Sub decorator two"""
    sub_system: BaseClass

    def __init__(self, sub_system_instance: BaseClass) -> None:
        super().__init__()
        self.sub_system = sub_system_instance

    def method_one(self)-> None:
        """Method one """
        self.int_mem = 19421
        self.str_mem = 'SubDecoratorTwo: Method One'
        print(self.str_mem, ' ', self.int_mem)

    def method_two(self)-> None:
        """Method one """
        self.int_mem = 19422
        self.str_mem = 'SubDecoratorTwo: Method two'
        print(self.str_mem, ' ', self.int_mem)

    def sub_decorator_operation_two(self)-> None:
        """Sub system operation """
        print ("SubDecoratorOne: Operation two")

    def decorator_display_two(self)-> None:
        """display method"""
        print('Decorator: Display two')

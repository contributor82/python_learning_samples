"""Module for sub decorator one class"""

from base_class import BaseClass
from decorator_class import Decorator

class SubDecoratorOne(Decorator):
    """Sub decorator one"""
    sub_system: BaseClass

    def __init__(self, sub_system_instance: BaseClass) -> None:
        super().__init__()
        self.sub_system = sub_system_instance

    def method_one(self)-> None:
        """Method one """
        self.int_mem = 19411
        self.str_mem = 'SubDecoratorOne: Method One'
        print(self.str_mem, ' ', self.int_mem)

    def method_two(self)-> None:
        """Method one """
        self.int_mem = 19412
        self.str_mem = 'SubDecoratorOne: Method two'
        print(self.str_mem, ' ', self.int_mem)

    def sub_decorator_operation_one(self)-> None:
        """Sub system operation """
        print ("SubDecoratorOne: Operation one")

    def decorator_display_one(self)-> None:
        """display method"""
        print('Decorator: Display one')

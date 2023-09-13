"""Module for decorator """

from base_class import BaseClass
from abc import ABC, abstractmethod

# Decorator class made abstract
# Also, inherited from BaseClass.
class Decorator(ABC, BaseClass):
    """Decorator class """

    @abstractmethod
    def method_one(self)-> None:
        """Method one """
        self.int_mem = 2
        self.str_mem = 'Base Method One'
        print(self.str_mem, ' ', self.int_mem)

    @abstractmethod
    def method_two(self)-> None:
        """Method one """
        self.int_mem = 2
        self.str_mem = 'Base Method two'
        print(self.str_mem, ' ', self.int_mem)

    def decorator_operation(self)-> None:
        """Sub system operation """
        print ("Decorator: Operation ")

    def decorator_display(self)-> None:
        """display method"""
        print('Decorator: Display')

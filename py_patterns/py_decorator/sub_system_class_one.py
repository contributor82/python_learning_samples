"""Module for sub system class one """

from base_class import BaseClass


class SubSystemClassOne(BaseClass):
    """Sub system class one"""
    int_mem: int
    str_mem: str

    def method_one(self)-> None:
        """Method one """
        self.int_mem = 191931
        self.str_mem = 'SubSystemClassOne: Method One'
        print(self.str_mem, ' ', self.int_mem)

    def method_two(self)-> None:
        """Method one """
        self.int_mem = 191931
        self.str_mem = 'SubSystemClassOne: Method two'
        print(self.str_mem, ' ', self.int_mem)

    def sub_system_operation_one(self)-> None:
        """Sub system operation one """
        print ("SubSystemClassOne: Operation one ")

    def sub_system_display_one(self)-> None:
        """display one method"""
        print('SubSystemClassOne: Display one')

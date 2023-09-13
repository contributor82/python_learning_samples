"""Module for sub system class two """

from base_class import BaseClass


class SubSystemClassTwo(BaseClass):
    """Sub system class two"""
    int_mem:int
    str_mem:str

    def method_one(self)-> None:
        """Method one """
        self.int_mem = 191932
        self.str_mem = 'SubSystemClassTwo: Method One'
        print(self.str_mem, ' ', self.int_mem)

    def method_two(self)-> None:
        """Method one """
        self.int_mem = 191932
        self.str_mem = 'SubSystemClassTwo: Method two'
        print(self.str_mem, ' ', self.int_mem)

    def sub_system_operation_two(self)-> None:
        """Sub system operation one """
        print ("SubSystemClassTwo: Operation two ")

    def sub_system_display_two(self)-> None:
        """display one method"""
        print('SubSystemClassTwo: Display two')

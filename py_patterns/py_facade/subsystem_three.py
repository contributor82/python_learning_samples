"""Module for Subsystem Three """

from sub_system import Subsystem

class SubsystemThree(Subsystem):
    """Subsystem three class"""

    def __init__(self) -> None:
        """Initializing Subsystem three class """
        print("Initializing Subsystem three ")

    def operation_one(self)-> None:
        """Operation one method"""
        print('SubsystemThree: Operation one complete')

    def operation_two(self)-> None:
        """Operation two method"""
        print('SubsystemThree: Operation two complete')

    def operation_three(self)-> None:
        """Operation three method"""
        print('SubsystemThree: Operation three complete')

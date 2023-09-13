"""Module for feature as well as decorator base class"""

class BaseClass:
    """Base class for feature as well as decorator"""
    int_mem_base: int
    str_mem_base: str

    def __init__(self) -> None:
        """Initializing Base product members """
        self.int_mem_base = 0
        self.str_mem_base = ""

    def method_one(self)-> None:
        """Method one """
        self.int_mem_base = 2
        self.str_mem_base = 'Base Method One'
        print(self.str_mem_base, ' ', self.int_mem_base)

    def method_two(self)-> None:
        """Method one """
        self.int_mem_base = 2
        self.str_mem_base = 'Base Method two'
        print(self.str_mem_base, ' ', self.int_mem_base)

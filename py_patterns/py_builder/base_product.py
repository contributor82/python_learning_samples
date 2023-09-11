"""Module for base product """

class BaseProduct:
    """Base Product class """
    int_member:int
    str_member:str

    def __init__(self) -> None:
        """Initializing Base product members """
        self.int_member = 0
        self.str_member = ""

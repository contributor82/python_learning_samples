"""Module for Derived product two """

from base_product import BaseProduct

class DerivedProductTwo(BaseProduct):
    """Derived Product two class """
    derived_two_int_member:int
    derived_two_str_member:str

    def __init__(self) -> None:
        """Initializing Derived product two members """
        self.derived_two_int_member = 0
        self.derived_two_str_member = ""

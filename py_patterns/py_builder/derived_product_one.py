"""Module for Derived product one """

from base_product import BaseProduct

class DerivedProductOne(BaseProduct):
    """Derived Product one class """
    derived_one_int_member:int
    derived_one_str_member:str

    def __init__(self) -> None:
        """Initializing Derived product one members """
        self.derived_one_int_member = 0
        self.derived_one_str_member = ""


"""Module for Single inheritance in Python"""
# Base Class added with members and display method.
class BaseClass:
    """ Base class """
    int_base_member: int = 1
    str_base_member: str = "Base Class"

    def display_base(self) -> str:
        """ Display base class string member """
        return self.str_base_member

# Derived Class inherited from base class and added its members & display method.
class DerivedClass(BaseClass):
    """ Derived class """
    int_derived_member: int =2
    str_derived_member: str = "Derived Class"

    def display_derived(self) -> str:
        """ Displaying derived class string member """
        return self.str_derived_member

if __name__ == '__main__':
    # Derived Class instance created.
    derived_instance = DerivedClass()

    # Invoked Base class method
    print("Base Class method invocation: ",  derived_instance.display_base())

    # Invoked Derived class method.
    print("Derived Class method invocation: ",  derived_instance.display_derived())
"""Module for multilevel inheritance in Python """
# Base Class added with members and display method.
class BaseClass:
    """ Base class """

    int_base_member: int = 1
    str_base_member: str = "Base Class"

    def get_str_base_member(self) -> str:
        """ Display base class string member """
        return self.str_base_member

    def get_int_base_member(self)-> int:
        """ Get int base member """
        return self.int_base_member

    def display_base(self)-> None:
        """Display base members """
        print("Int: ", self.int_base_member, " String: ", self.str_base_member)

class DerivedClass1(BaseClass):
    """ Derived class one """

    int_derived1_member: int =1
    str_derived1_member: str = "Derived Class One"

    def display_derived1(self) -> str:
        """Display derived one class string member method """
        return self.str_derived1_member

# Derived Class inherited from base class and added its members & display method.
class DerivedClass2(DerivedClass1):
    """ Derived class two """

    intDerived2Member: int =2
    strDerived2Member: str = "Derived Class Two"

    def display_derived2(self) -> str:
        """ Display derived class 2 string member method. """
        return self.strDerived2Member


if __name__ == '__main__':
    # Derived Class instance created.
    derived1_instance = DerivedClass1()

    # Derived Class instance created.
    derived2_instance = DerivedClass2()

    # Invoked Base class method
    print("Base Class method invocation using first derived class object : ")
    derived1_instance.display_base()

    # Invoked Derived class one method.
    print("Derived Class One method invocation: ",  derived1_instance.display_derived1())

    # Invoked Base class method
    print("Base Class method invocation using second derived class object : ",
          derived2_instance.display_base())

    # Invoked Derived class one method.
    print("Derived Class One method invocation: ",  derived2_instance.display_derived1())

    # Invoked Derived class two method.
    print("Derived Class Two method invocation: ",  derived2_instance.display_derived2())

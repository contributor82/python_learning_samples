
# Base Class added with members and display method. 
class BaseClass: 
    int_base_member: int = 1
    str_base_member: str = "Base Class"

    def display_base(self) -> str: 
        return self.str_base_member

# Derived Class inherited from base class and added its members & display method. 
class DerivedClass1(BaseClass): 
    int_derived1_member: int =1
    str_derived1_member: str = "Derived Class One"

    def display_derived1(self) -> str: 
        return self.str_derived1_member

# Derived Class inherited from base class and added its members & display method. 
class DerivedClass2(DerivedClass1): 
    intDerived2Member: int =2
    strDerived2Member: str = "Derived Class Two"

    def display_derived2(self) -> str: 
        return self.strDerived2Member


if __name__ == '__main__': 
    # Derived Class instance created. 
    derived1_instance = DerivedClass1()

    # Derived Class instance created. 
    derived2_instance = DerivedClass2()

    # Invoked Base class method
    print("Base Class method invocation using first derived class object : ",  derived1_instance.display_base())

    # Invoked Derived class one method. 
    print("Derived Class One method invocation: ",  derived1_instance.display_derived1())

    # Invoked Base class method
    print("Base Class method invocation using second derived class object : ",  derived2_instance.display_base())

    # Invoked Derived class one method. 
    print("Derived Class One method invocation: ",  derived2_instance.display_derived1())

    # Invoked Derived class two method. 
    print("Derived Class Two method invocation: ",  derived2_instance.display_derived2())


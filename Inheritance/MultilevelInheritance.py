
# Base Class added with members and display method. 
class BaseClass: 
    intBaseMember = 1
    strBaseMember = "Base Class"

    def displayBase(self): 
        return self.strBaseMember

# Derived Class inherited from base class and added its members & display method. 
class DerivedClass1(BaseClass): 
    intDerived1Member=1
    strDerived1Member = "Derived Class One"

    def displayDerived1(self): 
        return self.strDerived1Member

# Derived Class inherited from base class and added its members & display method. 
class DerivedClass2(DerivedClass1): 
    intDerived2Member=2
    strDerived2Member = "Derived Class Two"

    def displayDerived2(self): 
        return self.strDerived2Member

# Derived Class instance created. 
derived1ClassObject = DerivedClass1()

# Derived Class instance created. 
derived2ClassObject = DerivedClass2()

# Invoked Base class method
print("Base Class method invocation using first derived class object : ",  derived1ClassObject.displayBase())

# Invoked Derived class one method. 
print("Derived Class One method invocation: ",  derived1ClassObject.displayDerived1())

# Invoked Base class method
print("Base Class method invocation using second derived class object : ",  derived2ClassObject.displayBase())

# Invoked Derived class one method. 
print("Derived Class One method invocation: ",  derived2ClassObject.displayDerived1())

# Invoked Derived class two method. 
print("Derived Class Two method invocation: ",  derived2ClassObject.displayDerived2())


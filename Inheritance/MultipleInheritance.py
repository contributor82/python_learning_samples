
# Base Class 1 added with members and display method. 
class BaseClass1: 
    intBase1Member = 1
    strBase1Member = "Base Class One"

    def displayBase1(self): 
        return self.strBase1Member

# Base Class 2 added with members and display method. 
class BaseClass2: 
    intBase2Member = 2
    strBase2Member = "Base Class Two"

    def displayBase2(self): 
        return self.strBase2Member


# Derived Class inherited from base class and added its members & display method. 
class DerivedClass(BaseClass1, BaseClass2): 
    intDerivedMember=2
    strDerivedMember = "Derived Class"

    def displayDerived(self): 
        return self.strDerivedMember
    
# Derived Class instance created. 
derivedClassObject = DerivedClass()

# Invoked Base class One method
print("Base Class One method invocation: ",  derivedClassObject.displayBase1())

# Invoked Base class Two method
print("Base Class Two method invocation: ",  derivedClassObject.displayBase2())

# Invoked Derived class method. 
print("Derived Class method invocation: ",  derivedClassObject.displayDerived())
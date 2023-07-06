
# Base Class added with members and display method. 
class BaseClass: 
    intBaseMember = 1
    strBaseMember = "Base Class"

    def displayBase(self): 
        return self.strBaseMember

# Derived Class inherited from base class and added its members & display method. 
class DerivedClass(BaseClass): 
    intDerivedMember=2
    strDerivedMember = "Derived Class"

    def displayDerived(self): 
        return self.strDerivedMember
    
# Derived Class instance created. 
derivedClassObject = DerivedClass()

# Invoked Base class method
print("Base Class method invocation: ",  derivedClassObject.displayBase())

# Invoked Derived class method. 
print("Derived Class method invocation: ",  derivedClassObject.displayDerived())
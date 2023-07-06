class ParentClass: 
    intParentMember = 1
    stringParentMember = "Parent Class String member"
    def __init__(self) -> None:
        pass

    def parentDisplay(self):
        return self.stringParentMember
    
    # Inner class or child class or even called as nested class since it is inside the parent class. 
    class ChildClass:
        intChildMember = 2
        stringChildMember = "Child Class String member"

        def __init_subclass__(cls) -> None:
            pass

        def childDisplay(self): 
            return self.stringChildMember
    
parentClassObject = ParentClass()

print("Parent class String value: ", parentClassObject.parentDisplay())

childClassObject = parentClassObject.ChildClass()

print("Child class String value: ", childClassObject.childDisplay())

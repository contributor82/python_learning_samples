# Class creation in Python

class TestClass: 
    # Class member
    intMember = 12345

    # Default Constructor
    def __init__(self) -> None:
        pass

    # Method
    def display(self): 
        return "Hello World"
    
# Class Instance creation
testClassObject = TestClass()

print(testClassObject.intMember)
print(testClassObject.display())
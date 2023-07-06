# Class creation in Python

class TestClass: 
    # Class member
    intMember = 12345

    # Default Constructor
    def __init__(self) -> None:
        pass

    # Parameterized Constructor. 
    def __init__(self, int_member):
        self.intMember = int_member 

    # Method
    def display(self): 
        bugger = "Hello World!"
        return "Hello World"
    
# Class Instance creation
testClassObject = TestClass(34234)

print(testClassObject.intMember)
print(testClassObject.display())
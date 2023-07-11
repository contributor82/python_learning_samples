# Class creation in Python

class TestClass: 
    # Class member
    intMember: int
    strMember: str

    # Default Constructor
    def __init__(self) -> None:
        pass

    # Parameterized Constructor. 
    def __init__(self, int_member, str_member):
        self.intMember = int_member
        self.strMember = str_member 

    # Method
    def display(self): 
        print ("Integer member: ", self.intMember)
        print ("String member: ", self.strMember)
        
    
# Class Instance creation
testClassObject = TestClass(34234, "Test class")
testClassObject.display()

testClassObject.intMember = 123123
testClassObject.strMember = "Test class updated"

testClassObject.display()

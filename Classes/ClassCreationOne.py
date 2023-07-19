# Class creation in Python

class TestClass: 
    # Class member
    intMember: int
    strMember: str

    # Default Constructor
    def __init__(self)-> None: 
        pass

    # Parameterized Constructor. 
    def __init__(self, int_member : int, str_member: str) -> None:
        self.intMember = int_member
        self.strMember = str_member 

    # Method
    def display(self) -> None: 
        print ("Integer member: ", self.intMember)
        print ("String member: ", self.strMember)
        

if __name__ == '__main__':    
# Class Instance creation
    tcInstance = TestClass(34234, "Test class")
    tcInstance.display()

    tcInstance.intMember = 123123
    tcInstance.strMember = "Test class updated"

    tcInstance.display()

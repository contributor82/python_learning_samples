# Class creation in Python

class TestClass: 
    # Class member
    intMember = 12345

    # Default Constructor
    def __init__(self) -> None:
        pass

    # Method
    def display(self) -> str: 
        return "Hello World"
    

if __name__ == '__main__': 

    # Class Instance creation
    tcInstance = TestClass()

    print(tcInstance.intMember)
    print(tcInstance.display())
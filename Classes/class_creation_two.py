# Class creation in Python

class TestClass: 
    # Class member
    int_member = 12345

    # Default Constructor
    def __init__(self) -> None:
        pass

    # Method
    def display(self) -> str: 
        return "Hello World"
    

if __name__ == '__main__': 

    # Class Instance creation
    tc_instance = TestClass()

    print(tc_instance.int_member)
    print(tc_instance.display())
# Class creation in Python

class TestClass: 
    # Class member
    int_member: int = 12345

    def __init__(self) -> None:
        ### Default Constructor ###
        pass

    def display(self) -> str: 
        ### display method of Test class ###
        return "Hello World"
    

if __name__ == '__main__': 

    # Class Instance creation
    tc_instance = TestClass()

    print(tc_instance.int_member)
    print(tc_instance.display())
# Class creation in Python

class TestClass:
    # Class member
    int_member: int
    str_member: str

    def __init__(self) -> None: # type: ignore
        ### Default constructor ###
        pass

    def __init__(self, int_member: int, str_member: str) -> None: # type: ignore
        ### Parameterized Constructor. ###
        self.int_member = int_member
        self.str_member = str_member

    def display(self) -> None:
        ### Display class members. ###
        print("Integer member: ", self.int_member)
        print("String member: ", self.str_member)


if __name__ == '__main__':
    # Class Instance creation
    # tc_instance_one = TestClass() # Not permitted to create an instance with default constructor.

    tc_instance = TestClass(34234, "Test class")
    tc_instance.display()

    tc_instance.int_member = 123123
    tc_instance.str_member = "Test class updated"

    tc_instance.display()

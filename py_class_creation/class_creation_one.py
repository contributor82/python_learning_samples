""" Module for class creation in Python """

class TestClass:
    """ Test Class  """
    int_member: int = 0
    str_member: str = ''

    def __instancecheck__(self, __instance: object) -> bool:
        """Instance check method """
        return isinstance(__instance, type(self))

    def __init__(self) -> None:
        self.int_member = 0
        self.str_member = ''

    # Commented to try to get single instance.
    # def __init__(self, int_member: int, str_member: str) -> None:
    #     """ Parameterized Constructor. """
    #     self.int_member = int_member
    #     self.str_member = str_member

    def get_int_member(self) -> int:
        """ Get int member """
        return self.int_member

    def get_str_member(self) -> str:
        """ Get str member """
        return self.str_member

    def display(self) -> None:
        """ Display class members. """
        print('Integer member: ', self.int_member)
        print('String member: ', self.str_member)


if __name__ == '__main__':
    # Class Instance creation
    # tc_instance_one = TestClass() # Not permitted to create an instance with default constructor.
    # tc_instance = # TestClass(34234, 'Test class')
    tc_instance_one = TestClass()
    print('Initialization: ')
    tc_instance_one.display()

    tc_instance_one.int_member = 34234
    tc_instance_one.str_member = 'Test Class'
    print('After chaning values: ')
    tc_instance_one.display()

    tc_instance_two = TestClass()
    tc_instance_two.int_member = 54858056
    tc_instance_two.str_member = 'Test class two'
    tc_instance_two.display()

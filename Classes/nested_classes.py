"""Module for Nested classes in Python """
class ParentClass:
    """ Parent class """

    int_parent_member: int = 1
    str_parent_member: str = "Parent Class String member"

    def __init__(self) -> None:
        pass

    def get_parent_int_member(self) -> int:
        """ Get int member """
        return self.int_parent_member

    def get_parent_str_member(self) -> str:
        """ Get int member """
        return self.str_parent_member

    def parent_display(self) -> None:
        """ Parent display """
        print("int: ", self.int_parent_member, "str: ", self.str_parent_member)

    class ChildClass:
        """ Child class """
        # Inner class or child class or even called as nested class
        # since it is inside the parent class.

        int_child_member: int = 2
        str_child_member: str = "Child Class String member"

        def __init_subclass__(cls) -> None:
            pass

        def get_child_int_member(self) -> int:
            """ Get child int member """
            return self.int_child_member

        def get_child_str_member(self) -> str:
            """ Get child str member """
            return self.str_child_member

        def child_display(self) -> None:
            """ Child display """
            print("int: ", self.int_child_member, "str: ", self.str_child_member)

if __name__ == '__main__':
    parent_instance = ParentClass()
    print("Parent class String value: ")
    parent_instance.parent_display()
    child_instance = parent_instance.ChildClass()
    print("Child class String value: ")
    child_instance.child_display()

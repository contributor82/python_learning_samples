"""Module for Static class """

class StaticClass:
    """Static Class """
    int_mem: int

    def __init__(self) -> None:
        self.int_mem = 0

    @staticmethod
    def display()-> None:
        """static display method """
        print('Hello World! This is a static method. ')

    # @staticmethod
    # def display_members(self) -> None: #type: ignore
    #     """static display members method """
    #     print("Static Class Members : int_mem : ", self.int_mem) #type: ignore


    @staticmethod
    def display_class_members(class_int_mem : int ) -> None:
        """static display members method """
        print("Static Class Members : int_mem : ", class_int_mem)


if __name__ == '__main__':

    # By passing class instance, members can be accessed but it shouldn't be used.
    # Default Python doesn't seems permit to access class members.
    StaticClass.int_mem = 10
    StaticClass.display()
    # not recommended.
    # StaticClass.display_members(StaticClass) #type: ignore


    print('Creating static class instance as a separate instance variable' +
          '\n and then calling its respective methods. ')
    static_cls_instance = StaticClass()
    static_cls_instance.display()
    # not recommended.
    # static_cls_instance.display_members(StaticClass) #type: ignore
    static_cls_instance.display_class_members(StaticClass.int_mem)

    StaticClass().display()
    # not recommended.
    # StaticClass().display_members(StaticClass) #type: ignore
    StaticClass().display_class_members(StaticClass.int_mem)

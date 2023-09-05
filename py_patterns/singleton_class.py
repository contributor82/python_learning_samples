""" Module for Singleton class creation in Python """
from typing import Self # type: ignore

class SingletonClass:
    """ Singleton Class  """
    integer_member: int = 0
    string_member: str = ''
    instance: object = None

    def __instancecheck__(self, __instance: object) -> bool:
        """Instance check method """
        return isinstance(__instance, type(self))

    def __new__(cls) -> Self:
        """New method """
        returnable_obj: Self
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        returnable_obj = cls.instance # type: ignore
        return returnable_obj # type: ignore

    def get_instance(self, instance: object) -> Self:
        """Getting single instance of a class """
        if not instance is self:
            instance = SingletonClass()
        return instance # type: ignore

    def get_integer_member(self) -> int:
        """ Get int member """
        return self.integer_member

    def get_string_member(self) -> str:
        """ Get str member """
        return self.string_member

    def display(self) -> None:
        """ Display class members. """
        print('Integer member: ', self.integer_member)
        print('String member: ', self.string_member)


if __name__ == '__main__':

    sc_instance_one = SingletonClass()

    sc_instance_one.integer_member = 34234
    sc_instance_one.string_member = 'Singleton Class'

    sc_instance_two = SingletonClass()
    # sc_instance_three = SingletonClass()

    new_instance = object()
    # print('Is instance: ',  isinstance(sc_instance_one, SingletonClass))
    # print('Is instance: ',  sc_instance_one.__instancecheck__(new_instance))

    sc_instance_one.display()

    # tc_instance_one.integer_member = 123123
    # tc_instance_one.string_member = 'Singleton class one'

    sc_instance_one.display()

    # tc_instance_two: SingletonClass = tc_instance_one.get_instance(tc_instance_one)

    # tc_instance_two.integer_member = 54858056
    # tc_instance_two.string_member = 'Singleton class two'

    sc_instance_two.display()

    sc_instance_three = sc_instance_one.get_instance(sc_instance_one)

    print("sc_instance_one is sc_instance_two", sc_instance_one is sc_instance_two)
    print("sc_instance_two is sc_instance_three", sc_instance_two is sc_instance_three)

""" Module for Singleton class creation in Python """

from typing import Self

class SingletonClass:
    """ Singleton Class  """
    int_member: int = 0
    str_member: str = ''
    instance: object = None

    def __instancecheck__(self, __instance: object) -> bool:
        """Instance check method """
        return isinstance(__instance, type(self))

    def __new__(cls) -> Self:
        """New method """
        if not cls.instance is None:
            return cls.instance # type: ignore
        else:
            cls.instance = super().__new__(cls)
            return cls.instance


    def get_instance(self, instance: object) -> Self:
        """Getting single instance of a class """
        if not instance is self:
            instance = SingletonClass()
        return instance # type: ignore

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

    sc_instance_one = SingletonClass()

    sc_instance_one.int_member = 34234
    sc_instance_one.str_member = 'Singleton Class'

    sc_instance_two = SingletonClass()
    # sc_instance_three = SingletonClass()

    new_instance = object()
    # print('Is instance: ',  isinstance(sc_instance_one, SingletonClass))
    # print('Is instance: ',  sc_instance_one.__instancecheck__(new_instance))

    sc_instance_one.display()

    # tc_instance_one.int_member = 123123
    # tc_instance_one.str_member = 'Singleton class one'

    sc_instance_one.display()

    # tc_instance_two: SingletonClass = tc_instance_one.get_instance(tc_instance_one)

    # tc_instance_two.int_member = 54858056
    # tc_instance_two.str_member = 'Singleton class two'

    sc_instance_two.display()

    sc_instance_three = sc_instance_one.get_instance(sc_instance_one)

    print("sc_instance_one is sc_instance_two", sc_instance_one is sc_instance_two)
    print("sc_instance_two is sc_instance_three", sc_instance_two is sc_instance_three)

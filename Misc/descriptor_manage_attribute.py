"""Module for descriptor manage attribute """
import logging

logging.basicConfig(level=logging.INFO)

class LoggedAgeAccess:
    """Logged Age Access """

    # def __init__(self) -> None:
    #     """Initializing logging """

    def __get__(self, obj: object, objtype: object | None = None)-> None | object:
        """Logging and getting person age """
        value: object = obj.age #type: ignore
        logging.info('Accessing %r giving %r', 'age', value)
        return value

    def __set__(self, obj: object, value: object) -> None:
        """Logging and setting persson age """
        logging.info('updating %r to %r', 'age', value)
        obj.age = value #type : ignore


class Person:
    """Person class """
    age = LoggedAgeAccess()
    name: str = ""

    def __init__(self, person_name: str, person_age: int) -> None:
        """Initializing age and name """
        self.name = person_name
        self.age = person_age


    def birthday(self) -> None:
        """Person's birthday so increasing age by one """
        self.age = self.age + 1 #type: ignore


if __name__ == '__main__':
    person_one = Person('Person one', 26)
    print("Using Manage attribute: Person name: ",
          person_one.name, " age: ", person_one.age) #type: ignore
    person_one.birthday()
    print("After birthday call, Person name: ",
          person_one.name, " age: ", person_one.age) #type: ignore

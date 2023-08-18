"""Module for descriptor manage attribute """
import logging

# Converts function into bound methods

logging.basicConfig(level=logging.INFO)

class LoggedAccess:
    """Logged Access """
    public_name : str
    private_name : str
    # def __init__(self) -> None:
    #     """Initializing logging """

    def __set_name__(self, owner: object, name: str) -> None:
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj: object, objtype: object | None = None)-> None | object:
        """Logging and getting  age """
        value = getattr(obj, self.private_name) # Getting a named attribute
        logging.info('Accessing %r giving %r', self.public_name, value)
        return value

    def __set__(self, obj: object, value: object) -> None:
        """Logging and setting persson age """
        logging.info('Updating %r to %r', self.public_name, value)
        setattr(obj, self.private_name, value) # Sets the named attribute


class Person:
    """Person class """
    name: object | None = LoggedAccess()
    age: object | None = LoggedAccess()

    def __init__(self, person_name: str, person_age: int) -> None:
        """Initializing age and name """
        self.name = person_name
        self.age = person_age


    def birthday(self) -> None:
        """Person's birthday so increasing age by one """
        self.age = self.age + 1 #type: ignore

    def display_person_dtls(self)-> None:
        """Display person details """
        print("name: ", self.name, " age: ", self.age)


if __name__ == '__main__':
    vars(vars(Person)['name'])
    vars(vars(Person)['age'])
    person_first_instance = Person('Person one', 26)
    # print("Using Manage attribute: Person name: ",
    #       person_one.name, " age: ", person_one.age) #type: ignore
    person_first_instance.birthday()
    person_first_instance.display_person_dtls()
    # print("After birthday call, Person name: ",
    #       person_one.name, " age: ", person_one.age) #type: ignore
    person_second_instance = Person('Person second', 28)
    person_second_instance.birthday()
    person_second_instance.display_person_dtls()

"""Module for Student class for reference"""

class Student:
    """Student class """
    name: str = ''
    grade: str = ''
    age: int = 0

    def __init__(self, name : str, grade : str , age: int) -> None:
        """Class initialization """
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self) -> str:
        """Canonical string representation of string object method """
        return repr((self.name, self.grade, self.age))

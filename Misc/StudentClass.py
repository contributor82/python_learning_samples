class Student:
    name = ''
    grade = ''
    age = ''

    def __init__(self, name : str, grade : str , age: int) -> None:
         self.name = name
         self.grade = grade
         self.age = age

    def __repr__(self) -> str:
         return repr((self.name, self.grade, self.age))
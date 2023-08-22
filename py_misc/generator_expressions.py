"""Module for generator expressions """
# Expression have been added inside built-in functions.

from typing import Generator

class Student:
    """Student class """
    gpa: float =0
    name: str =''

    def __init__(self, gpa: float, name: str) -> None:
        self.gpa = gpa
        self.name = name

    def display_student(self) -> None:
        """Display Student """
        print('name: ', self.name, ' gpa: ', self.gpa)


    def calculate_gpa(self) -> None:
        """Calcualte gpa"""
        print('In progress')

class GeneratorExpressions:
    """Generator expressions class """

    def sum_expression(self, range_value: int) -> int:
        """Expression sum method """
        return sum(i*i for i in range(range_value))

    def sum_zip_expression(self, iter1: list[int], iter2: list[int]) -> int:
        """Expression sum zip method """
        return sum(x*y for x,y in zip(iter1,iter2))

    def max_expression(self,expression :
                       Generator[tuple[float | str, float | str], None,
                                 None]) -> tuple[float | str, float | str]:
        """Max expression method """
        return max(expression)

    def string_reversal(self, input_str: str) -> list[str]:
        """String reversal method """
        return list(input_str[i] for i in range(len(input_str)-1, -1, -1))


if __name__ == '__main__':
    ge_instance = GeneratorExpressions()
    print('Sum Expression: ', ge_instance.sum_expression(10))

    xvec: list[int] = [10,20,30]
    yvec: list[int] = [7,5,3]

    print('Sum zip expression: ', ge_instance.sum_zip_expression(xvec, yvec))

    # page is not defined by pylance
    # unique_words = set(word for line in page for word in line.split())
    graduates: list[dict[str, float | str]] = [ {'gpa':3.5,'name':'john'},
                                               {'gpa':3.0, 'name':'Scott'},
                 {'gpa': 4.5, 'name': 'Michael'}, {'gpa':2.9,'name':'Alan'} ]

    # Expression in max function to get the student name earned max gpa.
    # valedictorian = max((student['gpa'], student['name']) for student in graduates)

    # print (valedictorian)
    print(graduates)
    print('Max GPA earned Student using max expression : ',
          ge_instance.max_expression((student['gpa'], student['name']) for student in graduates))

    str_to_reverse: str = 'golf'
    # # Reversing the string using expression in list.
    print('Original String: ', str_to_reverse,
          ' After expression using list to reverse the string: ',
          ge_instance.string_reversal(str_to_reverse))

    # # Reversing the string and printing character by character.
    # def reverse(data):
    #     for index in range(len(data)-1,-1,-1):
    #         yield data[index]

    # # Calling reverse function
    # reverseString = reverse('golf')

    # # Getting iterator object.
    # iter(reverseString)

    # #Printing reverse string letters using for loop
    # for letter in reverseString:
    #     print(letter)

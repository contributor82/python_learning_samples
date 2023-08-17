"""Module for built in functions in Python """
import itertools
import random
import sys

sys.path.append('./Misc')
from student_class import Student #type:ignore

# Any purpose of accessing this laptop or mirroring it?
# Stop stealing. IT is disturbing for me right now.
# Read the note on desktop. you will be responsible for it.
# I saw somebody remotely logged in to this machine
# even everything is disconnected. that is very strange.
class BuiltInFunctions:
    """Built in functions class """

    def string_upper(self,input_str: str) -> str:
        """String upper method """
        return input_str.upper()

    def is_even(self, num: int) -> bool:
        """Is even number method """
        return (num % 2)  == 0

    def get_even_numbers(self, input_range: int) -> list[int]:
        """Get even numbers for the given range method """
        return (list(filter(self.is_even, range(input_range))))

    def generate_random_number(self) -> float:
        """Generate random number method """
        return random.random()

    def generate_random_sample(self, input_range: int, num_limit: int) -> list[int]:
        """Generate random sample method for the given range and number limit """
        return random.sample(range(input_range), num_limit)

    def number_sorting(self, num_list: list[int] | dict[int, str]) -> list[int]:
        """sorted number list for the given number list."""
        return sorted(num_list)

    def number_sorting_in_reverse_order(self, num_list: list[int]) -> list[int]:
        """ Sorting numbers in reverse order method """
        return sorted(num_list, reverse=True)

    def tuple_sorting(self, tuple_data: list[tuple[str,str,int]]) -> list[tuple[str, str, int]]:
        """ Tuple sorting method """
        return sorted(tuple_data)

    def tuple_sorting_by_specific_sorting(self,
                                          input_data: list[tuple[str,str,int]] | list[Student],
                                          tuple_lambda_expression : int | str) -> list[object]:
        """Tuple sorting by specific field method"""
        return sorted(input_data, key=tuple_lambda_expression) # type: ignore

    def new_iterators(self, start: int, step_val:int) -> object:
        """New iterators method - DO NOT USE"""
        return itertools.count(start, step_val)


if __name__ == '__main__':
    try:
        bif_instance = BuiltInFunctions()
        print(list(map(bif_instance.string_upper, ['sentence', 'fragment'])))
        print("Is given number even? : ", bif_instance.is_even(5))
        print("Get even numbers for the given range: ", bif_instance.get_even_numbers(10))
        print("Random number: ", bif_instance.generate_random_number())

        random_sample: list[int] = bif_instance.generate_random_sample(1000,10)
        print ("Generate random sample: ", random_sample)
        print("Sorted random sample: ", bif_instance.number_sorting(random_sample))

        keyValuePairList: dict[int, str] = {4:'D', 1: 'A', 3: 'C', 5:
                                            'E', 7:'G', 6: 'F', 8: 'H', 9: 'I', 2: 'B'}
        print("Sorted Key Value pair: ", bif_instance.number_sorting(keyValuePairList))

        print("Sorted random sample in reverse order : ",
            bif_instance.number_sorting_in_reverse_order(random_sample))

        students: list[tuple[str,str, int]] = [
            ('Sachin', 'A', 15),
            ('Ramesh', 'B', 12),
            ('Gunesh', 'B', 10)
        ]

        print("Students tuple prior sorting : ", students)
        print("Sorted students tuple: ", bif_instance.tuple_sorting(students))
        print("Sorted students tuple by specific field (name): ",
            bif_instance.tuple_sorting_by_specific_sorting(students,
                                                            lambda
                                                            student: student[0])) # type: ignore

        student_objects: list[Student] = [
            Student('Sachin', 'A', 15),
            Student('Ramesh', 'B', 12),
            Student('Gunesh', 'B', 10)
        ]

        print("Students prior sorting by age : ", student_objects)
        print("Sorted students tuple by specific field (age): ",
            bif_instance.tuple_sorting_by_specific_sorting(student_objects,
                                                            lambda
                                                            student: student.age)) # type: ignore
        print("New Iterators: ", bif_instance.new_iterators(0,5))
    except ValueError as value_error:
        print(value_error)
    except TypeError as type_error:
        print(type_error)
    except SystemError as system_error:
        print(system_error)

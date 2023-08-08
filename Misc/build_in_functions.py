
# Any purpose of accessing this laptop or mirroring it? 
# Stop stealing. IT is disturbing for me right now. 
# Read the note on desktop. you will be responsible for it. 
# I saw somebody remotely logged in to this machine even everything is disconnected. that is very strange. 

import itertools
import random
import sys
sys.path.append('\\Misc\\student_class.py')
from student_class import Student


class BuiltInFunctions: 

    # Returning input string in upper case
    def string_upper(self,input_str: str) -> str: 
        return input_str.upper()
    
    # Returning given number is even or not 
    def is_even(self, num: int) -> bool: 
        return (num % 2)  == 0
    
    # Returning list of even number for the given range. 
    def get_even_numbers(self, input_range: int) -> list[int]: 
        return (list(filter(self.is_even, range(input_range))))
    
    # Returning random numbers
    def generate_random_number(self) -> float: 
        return random.random()
    
    # Returning random number sample list for the given range and number limit
    def generate_random_sample(self, input_range: int, num_limit: int) -> list[int]: 
        return random.sample(range(input_range), num_limit)
    
    # Returning sorted number list for the given number list. 
    def number_sorting(self, num_list: list[int] | dict[int, str]) -> list[int]:
        return sorted(num_list)
    
    # Returning sorted number list in reverse order for the given number list.
    def number_sorting_in_reverse_order(self, num_list: list[int]) -> list[int]: 
        return sorted(num_list, reverse=True)

    # Returning tuple sorting
    def tuple_sorting(self, iter: list[tuple[str,str,int]]): 
        return sorted(iter)

    # Returning tuple sorting by specific field. 
    def tuple_sorting_by_specific_sorting(self, input_data: list[tuple[str,str,int]] | list[Student], tuple_lambda_expression : object) -> list[object]: 
        return sorted(input_data, key=tuple_lambda_expression)

    # DO NOT USE: New Generator using itertools.count showing incorrect result 
    def new_iterators(self, start: int, step_val:int): 
        return itertools.count(start, step_val)


if __name__ == '__main__': 

    bif_instance = BuiltInFunctions()

    print(list(map(bif_instance.string_upper, ['sentence', 'fragment'])))

    print("Is given number even? : ", bif_instance.is_even(5))

    print("Get even numbers for the given range: ", bif_instance.get_even_numbers(10))

    print("Random number: ", bif_instance.generate_random_number())

    random_sample = bif_instance.generate_random_sample(1000,10)

    print ("Generate random sample: ", random_sample)

    print("Sorted random sample: ", bif_instance.number_sorting(random_sample))

    keyValuePairList = {4:'D', 1: 'A', 3: 'C', 5: 'E', 7:'G', 6: 'F', 8: 'H', 9: 'I', 2: 'B'}

    print("Sorted Key Value pair: ", bif_instance.number_sorting(keyValuePairList))

    print("Sorted random sample in reverse order : ", bif_instance.number_sorting_in_reverse_order(random_sample))

    students = [
        ('Sachin', 'A', 15), 
        ('Ramesh', 'B', 12), 
        ('Gunesh', 'B', 10)
    ]

    print("Students tuple prior sorting : ", students)

    print("Sorted students tuple: ", bif_instance.tuple_sorting(students))

    print("Sorted students tuple by specific field (name): ", bif_instance.tuple_sorting_by_specific_sorting(students, lambda student: student[0]))

    student_objects = [
        Student('Sachin', 'A', 15), 
        Student('Ramesh', 'B', 12), 
        Student('Gunesh', 'B', 10)
    ]

    print("Students prior sorting by age : ", student_objects)
    print("Sorted students tuple by specific field (age): ", bif_instance.tuple_sorting_by_specific_sorting(student_objects, lambda student: student.age))

    # print("New Iterators: ", bif_instance.new_iterators(0,5) )








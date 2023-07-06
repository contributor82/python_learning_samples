
# Any purpose of accessing this laptop or mirroring it? 
# Stop stealing. IT is disturbing for me right now. 
# Read the note on desktop. you will be responsible for it. 
# I saw somebody remotely logged in to this machine even everything is disconnected. that is very strange. 

import itertools
import random

class Student:
    name = ''
    grade = ''
    age = ''

    def __init__(self, name, grade, age):
         self.name = name
         self.grade = grade
         self.age = age

    def __repr__(self):
         return repr((self.name, self.grade, self.age))



class BuiltInFunctions: 

    # Returning input string in upper case
    def string_upper(self,input_str): 
        return input_str.upper()
    
    # Returning given number is even or not 
    def is_even(self, num): 
        return (num % 2)  == 0
    
    # Returning list of even number for the given range. 
    def get_even_numbers(self, input_range): 
        return (list(filter(self.is_even, range(input_range))))
    
    # Returning random numbers
    def generate_random_number(self): 
        return random.random()
    
    # Returning random number sample list for the given range and number limit
    def generate_random_sample(self, input_range, num_limit): 
        return random.sample(range(input_range), num_limit)
    
    # Returning sorted number list for the given number list. 
    def number_sorting(self, num_list):
        return sorted(num_list)
    
    # Returning sorted number list in reverse order for the given number list.
    def number_sorting_in_reverse_order(self, num_list): 
        return sorted(num_list, reverse=True)

    # Returning tuple sorting
    def tuple_sorting(self, tuple): 
        return sorted(tuple)

    # Returning tuple sorting by specific field. 
    def tuple_sorting_by_specific_sorting(self, tuple, tuple_lambda_expression): 
        return sorted(tuple, key=tuple_lambda_expression )

    # DO NOT USE: New Generator using itertools.count showing incorrect result 
    def new_iterators(self, start, step_val): 
        return itertools.count(start, step_val)

bifInstance = BuiltInFunctions()

print(list(map(bifInstance.string_upper, ['sentence', 'fragment'])))

print("Is given number even? : ", bifInstance.is_even(5))

print("Get even numbers for the given range: ", bifInstance.get_even_numbers(10))

print("Random number: ", bifInstance.generate_random_number())

random_sample = bifInstance.generate_random_sample(1000,10)

print ("Generate random sample: ", random_sample)

print("Sorted random sample: ", bifInstance.number_sorting(random_sample))

keyValuePairList = {4:'D', 1: 'A', 3: 'C', 5: 'E', 7:'G', 6: 'F', 8: 'H', 9: 'I', 2: 'B'}

print("Sorted Key Value pair: ", bifInstance.number_sorting(keyValuePairList))

print("Sorted random sample in reverse order : ", bifInstance.number_sorting_in_reverse_order(random_sample))

students = [
    ('Sachin', 'A', 15), 
    ('Ramesh', 'B', 12), 
    ('Gunesh', 'B', 10)
]

print("Sorted students tuple: ", bifInstance.tuple_sorting(students))

print("Sorted students tuple by specific field: ", bifInstance.tuple_sorting_by_specific_sorting(students, lambda student: student[0]))

student_objects = [
    Student('Sachin', 'A', 15), 
    Student('Ramesh', 'B', 12), 
    Student('Gunesh', 'B', 10)
]

print("Sorted students tuple by specific field: ", bifInstance.tuple_sorting_by_specific_sorting(student_objects, lambda student: student.age))

# print("New Iterators: ", bifInstance.new_iterators(0,5) )








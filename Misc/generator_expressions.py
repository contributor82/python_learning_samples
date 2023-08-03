
# Expression have been added inside built-in functions. 

from typing import Generator


class Student: 
    gpa: float =0
    name: str =''

    def __init__(self, gpa: float, name: str):
        self.gpa = gpa
        self.name = name


class GeneratorExpressions: 

    def sum_expression(self, range_value: int): 
        return sum(i*i for i in range(range_value))

    def sum_zip_expression(self, iter1: list[int], iter2: list[int]): 
        return sum(x*y for x,y in zip(iter1,iter2))

    def max_expression(self,expression :Generator[tuple[float | str, float | str], None, None]): 
        return max(expression)
    
    def string_reversal(self, data: str): 
        return list(data[i] for i in range(len(data)-1, -1, -1))


if __name__ == '__main__': 
    ge_instance = GeneratorExpressions()
    print("Sum Expression: ", ge_instance.sum_expression(10))

    xvec = [10,20,30]
    yvec = [7,5,3]

    print("Sum zip expression: ", ge_instance.sum_zip_expression(xvec, yvec)) 

    # page is not defined by pylance
    # unique_words = set(word for line in page for word in line.split())


    graduates = [ {'gpa':3.5,'name':'john'}, {'gpa':3.0, 'name':'Scott'}, {'gpa': 4.5, 'name': 'Michael'}, {'gpa':2.9,'name':'Alan'} ]

    # Expression in max function to get the student name earned max gpa. 
    # valedictorian = max((student['gpa'], student['name']) for student in graduates)

    # print (valedictorian)
    print(graduates)
    print("Max GPA earned Student using max expression : ", ge_instance.max_expression((student['gpa'], student['name']) for student in graduates))

    data = 'golf'
    # # Reversing the string using expression in list. 
    print("Original String: '", data, "' After expression using list to reverse the string: ", ge_instance.string_reversal(data))

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

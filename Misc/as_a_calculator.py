"""Module for Python as a calculator"""
from math import sqrt

class AsACalculator:
    """Python as a calculator class """

    def addition(self, num1: int, num2: int) -> int:
        """addition method """
        return num1 + num2

    def subtraction(self, num1:int, num2: int) -> int:
        """subtraction method """
        return num1 - num2

    def division(self, num1:int, num2: int)-> float:
        """division method """
        return num1 / num2

    def division_discarding_fraction(self, num1: int, num2: int) -> int:
        """Division distraction fraction method """
        return num1 // num2

    def mod_operation(self, num1: int, num2: int) -> int:
        """Mod operation method """
        return num1 % num2

    def expression_exec(self, num1: int, num2: int, num3: int)-> int:
        """Expression execution method """
        return num1 * num2 + num3

    def num_square(self, num: int) -> int:
        """Number square method """
        return num ** 2

    def power_of_num(self, num: int, power: int) -> int:
        """Power of number method """
        return num ** power

    def num_square_root(self, num: float)-> float:
        """Number square root method """
        return sqrt(num)

if __name__ == '__main__':
    try:
        calc_instance = AsACalculator()
        print ("Addition of two numbers (1,2) : ", calc_instance.addition(1,2))
        print("Number subtraction (2,1) : ", calc_instance.subtraction(2,1))
        print("Number division (5,2) : ", calc_instance.division(5,2))
        print("Number division discarding fraction (5,2) : ",
            calc_instance.division_discarding_fraction(5,2))
        print("Mod operation (15,3) : ",calc_instance.mod_operation(15,3))
        print("Expression execution (5,3,2): ", calc_instance.expression_exec(5,3,2))
        print("Number square (10): ", calc_instance.num_square(10))
        print ("Power of a number (10, 3): ", calc_instance.power_of_num(10,3))
        print("Number square root (25) : ", calc_instance.num_square_root(25))
    except ArithmeticError as arithmetic_error:
        print(arithmetic_error)

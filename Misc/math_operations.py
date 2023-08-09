"""Module for math operations """
from cmath import acos, acosh
import math

class MathOperations:
    """Math operations class """

    def ceiling_of_num(self, num: float) -> int:
        """Getting ceiling of number """
        return math.ceil(num)

    def flooring_of_num(self, num: float) -> int:
        """ Getting flooring of number """
        return math.floor(num)

    def binomial_coefficient(self, n_items : int, k_items: int) -> int:
        """Getting binomial coefficient method """
        # Returns the number of ways to choose k items
        # from n items without repetition and WITHOUT order
        return math.comb(n_items, k_items)

    def coefficient_perm(self, n_items: int, k_items: int | None)-> int:
        """Getting coefficient perm method """
        # Returns the number of ways to choose k items
        # from n items without repetition and WITH order
        return math.perm(n_items, k_items)

    def copy_sign(self, num1: float, num2: float) -> float:
        """Copy sign method """
        # Returns the magnitude of x but the sign of y
        return math.copysign(num1, num2)


    def arc_cosine(self, num: float)-> complex :
        """Getting Arc cosine method """
        # Returns arc cosine of number
        # measured in radians
        # Result is between 0 and pi
        return acos(num)

    def inverse_hyperbolic_cosine(self, num: float)-> complex:
        """Getting Inverse hyperbolic cosine method """
         # Returns the inverse hyperbolic cosine of number
        return acosh(num)

    def greatest_common_divisor(self, num1: int, num2: int, num3: int) -> int:
        """Getting Greatest common divisor """
        # Returns the greatest common divisor of given number arguments
        return math.gcd(num1, num2, num3)

    def least_common_multiple(self, num1: int, num2: int, num3: int) -> int:
        """Getting Least common multiple method """
        # Returns the least common multiple of given number arguments
        return math.lcm(num1, num2, num3)

    def product_of_all_elements(self, nums : list[int | float] ) -> int | float:
        """Getting product of all elements """
        # Returns the product of all elements,
        # * operator, default start position 1 unless specified.
        return math.prod(nums)

if __name__ == '__main__':
    mo_instance =  MathOperations()
    print("Ceiling of num (5.8) :", mo_instance.ceiling_of_num(5.8))
    print("Flooring of num (5.8) :", mo_instance.flooring_of_num(5.8))
    print("Arc cosine of num (15.0) : ", mo_instance.arc_cosine(15.0))
    print("Inverse hyperbolic cosine of num (15.0) : ", mo_instance.inverse_hyperbolic_cosine(15.0))
    print("Binomial Coefficient (100,10): ", mo_instance.binomial_coefficient(100, 10))
    print("Coefficient perm (100,None): ", mo_instance.coefficient_perm(100, None))
    print("Copy sign of x & y (10.50, -2.5) :  ", mo_instance.copy_sign(10.50, -2.5))
    print("Greatest common divisor of 15,5,25: ", mo_instance.greatest_common_divisor(15,5,25))
    print("Least common multiple of 15,10,0: ", mo_instance.least_common_multiple(15,10,0))
    print("Product of all elements [10,15,5.2,20] : ",
            mo_instance.product_of_all_elements([10,15,5.2,20]))

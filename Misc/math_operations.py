from cmath import acos, acosh

import math

class MathOperations: 

    # Returns the ceiling of a number
    def ceiling_of_num(self, num: float) -> int: 
        return math.ceil(num)
    
    # Returns the flooring of a number
    def flooring_of_num(self, num: float) -> int: 
        return math.floor(num)
    
    # Returns the number of ways to choose k items from n items without repetition and WITHOUT order 
    def binomial_coefficient(self, nItems : int, kItems: int) -> int: 
        return math.comb(nItems, kItems)
    
    # Returns the number of ways to choose k items from n items without repetition and WITH order
    def coefficient_perm(self, nItems: int, kItems:  int | None)-> int: 
        return math.perm(nItems, kItems)

    # Returns the magnitude of x but the sign of y
    def copy_sign(self, num1: float, num2: float) -> float: 
        return math.copysign(num1, num2)
    

    # Returns arc cosine of number
    # measured in radians
    # Result is between 0 and pi 
    def arc_cosine(self, num: float)-> complex : 
        return acos(num)
    
    # Returns the inverse hyperbolic cosine of number
    def inverse_hyperbolic_cosine(self, num: float)-> complex: 
        return acosh(num)
    
    # Returns the greatest common divisor of given number arguments
    def greatest_common_divisor(self, num1: int, num2: int, num3: int) -> int: 
        return math.gcd(num1, num2, num3) 
    
    # Returns the least common multiple of given number arguments
    def least_common_multiple(self, num1: int, num2: int, num3: int) -> int: 
        return math.lcm(num1, num2, num3)

    # Returns the product of all elements, * operator, default start position 1 unless specified.
    def product_of_all_elements(self, nums : list[int | float] ) -> int | float:
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
   print("Product of all elements [10,15,5.2,20] : ", mo_instance.product_of_all_elements([10,15,5.2,20]))



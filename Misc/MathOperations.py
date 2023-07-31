from cmath import acos, acosh

import math

class MathOperations: 

    # Returns the ceiling of a number
    def ceiling_of_num(self, num: float) -> int: 
        return math.ceil(num)
    
    # Returns the flooring of a number
    def flooring_of_num(self, num: float) -> int: 
        return math.floor(num)
    
    # Returns the number of ways to choose k items from n items without repetition and without order 
    def binomial_coefficient(self, nItems : int, kItems: int) -> int: 
        return math.comb(nItems, kItems)

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


if __name__ == '__main__': 
   moInstance =  MathOperations()

   print("Ceiling of num (5.8) :", moInstance.ceiling_of_num(5.8))
   print("Flooring of num (5.8) :", moInstance.flooring_of_num(5.8))
   print("Arc cosine of num (15.0) : ", moInstance.arc_cosine(15.0))
   print("Inverse hyperbolic cosine of num (15.0) : ", moInstance.inverse_hyperbolic_cosine(15.0))
   print("Binomial Coefficient (100,10): ", moInstance.binomial_coefficient(100, 10))
   print("Copy sign of x & y (10.50, -2.5) :  ", moInstance.copy_sign(10.50, -2.5))


"""Module for factorial of a number"""


class Factorial:
    """Class for factorial of a number"""
    num: int

    def __init__(self, number: int) -> None:
        """Init method for Factorial class"""
        self.num = number

    def factorial(self) -> int:
        """Method to calculate factorial of a number"""
        fact: int = 1
        for i in range(1, self.num+1):
            fact = fact * i
        return fact


if __name__ == "__main__":
    num = int(input("Enter a number to calculate its factorial : "))
    factorial_instance = Factorial(num)
    print("Factorial of a ", num, " is ", factorial_instance.factorial())

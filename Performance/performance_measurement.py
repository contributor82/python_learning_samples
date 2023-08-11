"""Module for performance meansurement """
from timeit import Timer

class PerformanceMeasurement:
    """Performance measurement class """

    def swap_numbers(self, num_one: int, num_two: int) -> None:
        """Swap numbers method """
        print ('Numbers before swapping : num_one = ', num_one, " num_two = ", num_two)
        temp: int
        temp = num_one
        num_one = num_two
        num_two = temp

        print ('Numbers after swapping : num_one = ', num_one, " num_two = ", num_two)


    def perf_check(self) -> None:
        """Performance check method """
        # Swap number function statements have been evaluated for performance.
        result: float = Timer('temp = num1; num1 = num2; num2 = temp ',
                              'num1 = 1; num2 = 2').timeit()
        print(result)

if __name__ == '__main__':
    perf_instance = PerformanceMeasurement()
    perf_instance.perf_check()

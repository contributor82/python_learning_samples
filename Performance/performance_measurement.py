from timeit import Timer

class PerformanceMeasurement: 

    def swap_numbers(self) -> None:
        num1 = 1, 
        num2 = 2
        print ('Numbers before swapping : num1 = ', num1, " num2 = ", num2) 
        
        temp = num1 
        num1 = num2 
        num2 = temp
        
        print ('Numbers after swapping : num1 = ', num1, " num2 = ", num2)


    def perf_check(self) -> None:
        # Swap number function statements have been evaluated for performance. 
        result = Timer('temp = num1; num1 = num2; num2 = temp ', 'num1 = 1; num2 = 2').timeit()
        print(result)
        
if __name__ == '__main__':  
    perfInstance = PerformanceMeasurement()
    perfInstance.perf_check()



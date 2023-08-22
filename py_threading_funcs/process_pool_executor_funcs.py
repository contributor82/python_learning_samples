"""Module for process pool executor """

import concurrent.futures
import math

# Uses Multiprocessing module permits to side step global interpreter lock
# global interpreter lock  - The mechanism used by CPYthon
# to ensure single thread executes Python Bytecode at a time
# Meaning only pickable objects can be executed.
# If max worker value is not given then the number of processors of the machine will be used.
# If max worker value is given then the max Worker worker thread can be used to process the task.
# max worker limit is 61

class ProcessPoolExecutorFuncs:
    """ Process pool executor sample class """
    prime_numbers: list[int]

    def __init__(self, prime_list: list[int]) -> None:
        """Initializing prime number list """
        self.prime_numbers = prime_list

    def is_prime_num(self, num: int) -> bool:
        """is given number prime or not method """
        is_prime: bool = True
        if num < 2:
            is_prime = False
        elif num == 2:
            is_prime = True
        elif num % 2 == 0:
            is_prime = False

        sqrt_n = int(math.floor(math.sqrt(num)))
        for i in range(3, sqrt_n + 1, 2 ):
            if num % i ==0:
                is_prime = False
                break
        return is_prime

    def execute_process_pool(self) -> None:
        """Execute process pool method """
        # Executing process tool executor to run thread asynchronously.
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for number, prime in zip(self.prime_numbers,
                                     executor.map(self.is_prime_num,
                                                  self.prime_numbers)):
                # print('%d is prime: %s' % (number, prime))
                print(f'{number} is prime: {prime}')

if __name__ == '__main__':
    try:
        process_pool_exec_instance = ProcessPoolExecutorFuncs([1,3,5,7,9])
        process_pool_exec_instance.execute_process_pool()
    except concurrent.futures.TimeoutError as time_out_error:
        print(time_out_error)
    except concurrent.futures.CancelledError as cancelled_error:
        print(cancelled_error)

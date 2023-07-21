
import concurrent.futures
import math

# Uses Multiprocessing module permits to side step global interpreter lock
# global interpreter lock  - The mechanism used by CPYthon to ensure single thread executes Python Bytecode at a time
# Meaning only pickable objects can be executed. 
# If max worker value is not given then the number of processors of the machine will be used. 
# If max worker value is given then the max Worker worker thread can be used to process the task. 
# max worker limit is 61

class ProcessPoolExecutorSample: 
    prime_numbers = [1,3,5,7,9]

    # is given number prime or not
    def is_prime_num(self, num: int) -> bool: 
        if num < 2: 
            return False
        elif num == 2: 
            return True
        elif num % 2 == 0: 
            return False
    
        sqrt_n = int(math.floor(math.sqrt(num))) 
        for i in range(3, sqrt_n + 1, 2 ): 
            if num % i ==0: 
                return False
        return True
    
    # Executing process tool executor to run thread asynchronously. 
    def execute_process_pool(self) -> None:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for number, prime in zip(self.prime_numbers, executor.map(self.is_prime_num, self.prime_numbers)):
                print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
  ppesInstance = ProcessPoolExecutorSample()
  ppesInstance.execute_process_pool()


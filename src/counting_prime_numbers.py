# https://python.plainenglish.io/count-primes-day-78-python-7c37eb7c2c07
# https://leetcode.com/problems/count-primes/

import time

class PrimeCounter:
    def __init__(self):
        pass
    def countPrimes(self, n: int) -> int:
        primes = [True for i in range(n)] # keep all the n values as True
        i = 2
        # Start from index 2, all the index numbers that are multiples of 2 are marked False. 
        # Similarly, we need to keep find the multiples of each number until we reach a number that 
        # is close to the square root of the input number
        # Loop's ending condition is i * i < n instead of i < sqrt(n)
        # to avoid repeatedly calling an expensive function sqrt().
        while(i*i < n):
            if(primes[i] == True): 
                for p in range(i*i, n, i):
                    primes[p] = False
            i += 1
        
        # counter = 0
        # for i in range(2, len(primes)):
        #     if primes[i]:
        #         counter += 1
        # return counter

        # finding sum of true values instead of for loop and incremental count
        print(sum(primes[2:])) #starting from index 2.


counter_obj = PrimeCounter()
start_time = time.time()
counter_obj.countPrimes(100)
print(f"{(time.time() - start_time)} seconds")
    
#time taken to find the prime numbers till 100000000 is --> 78.67293000221252 seconds
# above this limit 100000000, i am getting memory issue
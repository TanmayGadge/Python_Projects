from time import time
from math import sqrt

#Program to generate prime numbers upto a limit and write it in a file.


def Prime(number):
    i = 2
    isPrime = True
    while i <= sqrt(number):
        #Every number has at least one prime factor less than or equal to the sqrt of that number.

        if(number % i == 0):
            isPrime = False
            break
        elif(number % i != 0):
            i += 1

    return isPrime


def generatePrime(limit):
    primes = [i for i in range(2,limit+1) if(Prime(i))]
    return primes


start = time()
x = generatePrime(10**6)

# file = open('primes.txt', 'w+')
# file.write(f"Primes = {str(x)}")
# file.close()

with open('primes.txt', 'w') as file:
    file.write(f'Primes: {str(x)}')

print(f"{(time()-start)*1000} ms")#prints the time taken for writing all the primes.
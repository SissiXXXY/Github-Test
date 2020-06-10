"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
import math

primeList = []


def is_prime(num):
    threshold = int(math.sqrt(num))
    for b in primeList:
        """
        in python, for x in the list is to go over every element in the list
        so, if there are two for loops together, it is complex, it go over a and b instead of (a n b)
        """
        if num % b == 0:
            return False
        if b > threshold:
            break

    return True


def getprime():
    primeList.append(2)
    print(primeList)
    k = 2
    while True:
        k += 1
        if is_prime(k):
            primeList.append(k)
            print(k)
        if len(primeList) == 10001:
            break


getprime()
print(primeList[-1])


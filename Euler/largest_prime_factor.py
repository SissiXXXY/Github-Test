"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import math

primeList = []
pfactor = []


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
    for num in range(3, 600851475143):
        if is_prime(num):
            primeList.append(num)
            print(num)


def factoring(num):
    for k in primeList:
        if num % k == 0:
            if num / k in primeList:
                """if the quotient is prime """
                pfactor.append(num / k)
            else:
                """if the quotient is not prime, factor the quotient"""
                factoring(num / k)
        else:
            """if the num cannot be divided by the first prime, go to the next"""
            k += 1


getprime()
factoring(600851475143)
print(max(pfactor))

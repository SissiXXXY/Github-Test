"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
import math


def get_lcm(a, b):
    print((a * b) / math.gcd(a, b))
    return (a * b) / math.gcd(a, b)


temp = 2
for i in range(1, 21):
    i + 1
    print(i)
    temp = get_lcm(i, temp)
    i += 1
print(temp)

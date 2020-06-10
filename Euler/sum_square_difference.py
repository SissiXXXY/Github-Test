"""
The sum of the squares of the first ten natural numbers is,
12+22+...+102=385
The square of the sum of the first ten natural numbers is,
(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import math
squares = []
k = 1
while True:
    squares.append(k ** 2)
    k += 1
    print(k)
    if k > 100:
        break
print(squares)
sums = 0
for i in range(100):
    sums += i + 1
print(sums)
print(abs(sums ** 2 - sum(squares)))

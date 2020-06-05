import math
import time

primeList = []


def is_prime(num):
    threshold = int(math.sqrt(num))
    for b in primeList:
        if num % b == 0:
            return False
        if b > threshold:
            break

    return True


def getprime():
    primeList.append(2)
    print(primeList)
    for num in range(3, 100000):
        if is_prime(num):
            primeList.append(num)
            print(num)


start = time.time()
getprime()
print(sum(primeList))
end = time.time()
print(str(end - start))

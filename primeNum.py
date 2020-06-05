import math
import time

primeList = []
def notdivbefore( current ):
    if primeList:
        for b in primeList:
            if current%b==0 :
                return False

        return True

    else:
        return True


start = time.time()
def getprime():
    primeList.append(2)
    for num in range(2,100000):
        for k in range(2,int(math.sqrt(k))):
            if notdivbefore(num):
                primeList.append(num)


end = time.time()

print(str(end-start))

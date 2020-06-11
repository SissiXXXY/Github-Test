# -*- coding: utf-8 -*-

import time
from threading import Thread


def job(n: int):
    s = 0
    for x in range(n):
        s += x
        time.sleep(0.01)
        print(f"n={n}, sum 1..{x} = {s}")


if __name__ == '__main__':
    numbers = list(range(100, 200, 20))
    threads = []
    for n in numbers:
        th = Thread(target=job, args=(n,))
        th.start()
        threads.append(th)
    for th in threads:
        th.join()

    print("round 1 finished")
    input()

    numbers = list(range(200, 210, 2))
    for n in numbers:
        th = Thread(target=job, args=(n,))
        th.start()

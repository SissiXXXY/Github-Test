# -*- coding: utf-8 -*-
import threading
import time
from threading import Thread
import random

t = []
lock = threading.Lock()


def producer(id: str):
    print(f"producer {id} started")
    for i in range(10000):
        lock.acquire()
        a = random.randint(1, 500)
        b = random.randint(1, 500)
        print(f"num a = {a}, num b = {b}, sum = {a + b}")
        t.append(a + b)
        lock.release()


def consumer(id: str):
    while True:
        print(f"consumer {id} started")

        has_data = False
        x = 0

        lock.acquire()
        if len(t) > 0:
            has_data = True
            x = t[-1]
            del t[-1]
        lock.release()

        if has_data:
            work(x)


def work(last):
    print(f"the last is {last}, minus one is {last - 1}")


if __name__ == '__main__':
    # start consumers
    for i in range(3):
        consumer_thread = Thread(target=consumer, args=(f"C{i + 1}",))
        consumer_thread.start()
        """consumer_thread.join()"""

    # start producers
    time.sleep(1)
    for i in range(2):
        producer_thread = Thread(target=producer, args=(f"P{i + 1}",))
        producer_thread.start()
        """producer_thread.join()"""

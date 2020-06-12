# -*- coding: utf-8 -*-
import threading
import time
from threading import Thread
import random

t = []
lock = threading.Lock()
event = threading.Event()
num = 0


def producer(id: str):
    global num
    print(f"producer {id} started")
    while True:
        lock.acquire()
        num = num + 1
        print(f"producer {id} appending {num} into list")
        t.append(num)
        event.set()
        lock.release()
        time.sleep(random.random())


def consumer(id: str):
    print(f"consumer {id} started")
    while True:
        print(f"consumer {id} ready to get next data")
        has_data = False
        x = 0
        remaining = 0

        lock.acquire()
        if len(t) > 0:
            has_data = True
            x = t[0]
            del t[0]
            remaining = len(t)
            if remaining <= 0:
                event.clear()
        lock.release()
        if not event.isSet():
            event.wait()

        if has_data:
            work(id, x, remaining)


def work(id, cus, remaining):
    print(f"consumer {id} now serving customer: {cus}, {remaining} in queue")
    time.sleep(random.random() * 3)


if __name__ == '__main__':
    # start consumers
    for i in range(15):
        consumer_thread = Thread(target=consumer, args=(f"C{i + 1}",))
        consumer_thread.start()
        """consumer_thread.join()"""

    # start producers
    for i in range(5):
        producer_thread = Thread(target=producer, args=(f"P{i + 1}",))
        producer_thread.start()
        """producer_thread.join()"""

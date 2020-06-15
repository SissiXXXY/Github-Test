# -*- coding: utf-8 -*-
import threading
import time
from threading import Thread
import random

num = 0


def producer(id: str):
    global num
    print(f"producer {id} started")
    while True:
        # call push()
        example.push(num)
        num = num + 1
        time.sleep(random.random())


def consumer(id: str):
    print(f"consumer {id} started")
    while True:
        print(f"consumer {id} ready to get next data")
        # call pop
        x = example.pop()
        work(id, x)


def work(id, cus):
    print(f"consumer {id} now serving customer: {cus}")
    time.sleep(random.random() * 3)


class SimpleQueue:
    def __init__(self):
        self.t = []
        self.lock = threading.Lock()
        self.event = threading.Event()

    def push(self, content):
        with self.lock:
            print(f"producer {id} appending {content} into list")
            self.t.append(content)
            self.event.set()

    def count(self):
        with self.lock:
            return self.__count()

    def __count(self):
        return len(self.t)

    def pop(self):
        while True:
            self.event.wait()
            with self.lock:
                if self.__count() > 0:
                    x = self.t[0]
                    del self.t[0]
                    remaining = len(self.t)
                    if remaining <= 0:
                        self.event.clear()
                    print(x)
                    return x


if __name__ == '__main__':
    example = SimpleQueue()

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

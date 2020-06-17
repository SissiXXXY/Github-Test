# -*- coding: utf-8 -*-
import string
import threading
import time
from threading import Thread
import random
import heapq

def producer(id: str):
    print(f"producer {id} started")
    while True:
        produce()
        # time.sleep(random.random())


def produce():
    localtime = time.localtime(time.time())
    ran_str = ''.join(random.sample(string.ascii_letters, 4))
    while True:
        num = random.randint(1, 10000)
        common = Customer(num, ran_str, 'common', localtime)
        example.push(common)
        time.sleep(random.random())


def consumer(id: str):
    print(f"consumer {id} started")
    while True:
        print(f"consumer {id} ready to get next data")
        # call pop
        x = example.pop()
        work(id, x.number, x.type)


def work(id, customer, type):
    print(f"consumer {id} now serving customer number: {customer}, type: {type}")
    time.sleep(random.random() * 3)


class Customer:
    def __init__(self, number, name, type, arrival_time):
        self.number = number
        self.name = name
        self.type = type
        self.arrival_time = arrival_time
        self.lock = threading.Lock()


class SimpleQueue:
    def __init__(self):
        self.t = heapq
        self.lock = threading.Lock()
        self.event = threading.Event()

    def push(self, content):
        with self.lock:
            print(f"producer {id} appending {content.number} into list")
            heapq.heappush(self.t, content)
            self.event.set()

    """def count(self):
        with self.lock:
            return self.__count()

    def __count(self):
        return len(self.t)"""

    def pop(self):
        while True:
            self.event.wait()
            with self.lock:
                return heapq.heappop(self.t)

    """def poppri(self):
        while True:
            self.event.wait()
            with self.lock:
                if self.__count() > 0:
                    # the least num shows the highest priority
                    fir = min(self.priority)
                    i = self.t.index(Customer.number == fir)
                    x = self.t[i]
                    del self.t[i]
                    # self.t.remove(fir)
                    remaining = len(self.t)
                    if remaining <= 0:
                        self.event.clear()
                    print(x)
                    return x"""


if __name__ == '__main__':
    example = SimpleQueue()
    # start consumers
    for i in range(2):
        consumer_thread = Thread(target=consumer, args=(f"C{i + 1}",))
        consumer_thread.start()
        """consumer_thread.join()"""

    # start producers
    for i in range(3):
        producer_thread = Thread(target=producer, args=(f"P{i + 1}",))
        producer_thread.start()
        """producer_thread.join()"""

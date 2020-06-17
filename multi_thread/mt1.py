# -*- coding: utf-8 -*-
import string
import threading
import time
from datetime import datetime
from threading import Thread
import random
import heapq


class Customer:
    def __init__(self, number, name, type, arrival_time):
        self.number = number
        self.name = name
        self.type = type
        self.arrival_time = arrival_time
        self.lock = threading.Lock()

    def __lt__(self, other):
        if isinstance(other, Customer):
            if self.number < other.number:
                return True
            elif self.number == other.number:
                return self.name < other.name
            else:
                return False
        else:
            raise NotImplementedError()

    def __gt__(self, other):
        if isinstance(other, Customer):
            if self.number > other.number:
                return True
            elif self.number == other.number:
                return self.name > other.name
            else:
                return False
        else:
            raise NotImplementedError()

    def __eq__(self, other):
        if isinstance(other, Customer):
            return self.number == other.number and self.name == other.name
        else:
            raise NotImplementedError()

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return f"[{self.number}]{self.name} {self.type} {self.arrival_time}"


class SimpleQueue:
    def __init__(self):
        self.t = []
        self.lock = threading.Lock()
        self.event = threading.Event()

    def push(self, content):
        with self.lock:
            heapq.heappush(self.t, content)
            self.event.set()

    """def count(self):
        with self.lock:
            return self.__count()

    def __count(self):
        return len(self.t)"""

    def pop(self):
        while True:
            self.event.wait(1)
            with self.lock:
                if len(self.t) > 0:
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


def producer_func(id: str):
    print(f"producer {id} started")
    for i in range(10):
        c: Customer = produce()
        print(f"producer {id} appending {c} into list")
        global_queue.push(c)
        time.sleep(random.random())


def produce():
    num = random.randint(1, 10000)
    ran_str = ''.join(random.sample(string.ascii_letters, 4))
    return Customer(num, ran_str, 'common', datetime.now())


def consumer_func(id: str):
    print(f"consumer {id} started")
    while True:
        print(f"consumer {id} ready to get next data")
        c: Customer = global_queue.pop()
        work(id, c)


def work(id, customer):
    print(f"consumer {id} now serving customer: {customer}")
    time.sleep(random.random() * 3)


if __name__ == '__main__':
    global_queue = SimpleQueue()
    in_working_hours = True

    # start consumers
    for i in range(2):
        consumer_thread = Thread(target=consumer_func, args=(f"C{i + 1}",))
        consumer_thread.start()
        """consumer_thread.join()"""

    # start producers
    for i in range(3):
        producer_thread = Thread(target=producer_func, args=(f"P{i + 1}",))
        producer_thread.start()
        """producer_thread.join()"""

    while True:
        cmd = input()
        if cmd == "exit":
            print("==================exit====================")
            print("******* do something to exit *************")
            in_working_hours = False
            break
        else:
            print(f"=================={cmd}====================")

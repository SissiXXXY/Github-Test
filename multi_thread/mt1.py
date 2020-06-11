# -*- coding: utf-8 -*-
from threading import Thread


def producer(id: str):
    print(f"producer {id} started")
    for i in range(10000):
        ...


def consumer(id: str):
    print(f"consumer {id} started")


if __name__ == '__main__':
    # start consumers
    for i in range(3):
        consumer_thread = Thread(target=consumer, args=(f"C{i + 1}",))
        consumer_thread.start()

    # start producers
    for i in range(2):
        producer_thread = Thread(target=producer, args=(f"P{i + 1}",))
        producer_thread.start()

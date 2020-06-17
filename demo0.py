import heapq

class PQ:
    def push(self, n):
        ...

    def pop(self):
        ...

    def count(self):
        ...


def test_0():
    q = PQ()
    q.push(1)
    q.push(3)
    q.push(2)
    ret = [q.pop(), q.pop(), q.pop()]
    assert ret == [1, 2, 3]


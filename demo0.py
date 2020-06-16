class Producer0:
    n = 1

    def get_next(self):
        Producer0.n += 1
        return Producer0.n


if __name__ == '__main__':
    a = Producer0()
    b = Producer0()
    print(a.get_next())
    print(b.get_next())
    print(a.get_next())
    print(b.get_next())

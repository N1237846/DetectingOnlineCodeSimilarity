import cProfile


def prime_test(n):
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


class PrimesIterator:

    def __init__(self, limit):
        self.counter = 0
        self.current_prime = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.current_prime += 1
            while not prime_test(self.current_prime):
                self.current_prime += 1
            self.counter += 1
            return self.current_prime
        raise StopIteration()


def memory_usage():
    item_list = []
    for _ in range(1000000):
        item_list.append(object())
    return item_list


def primary_function():
    memory_usage()
    # list(PrimesIterator(1000))
    # cProfile.run('list(PrimesIterator(10000))')


if __name__ == '__main__':
    primary_function()

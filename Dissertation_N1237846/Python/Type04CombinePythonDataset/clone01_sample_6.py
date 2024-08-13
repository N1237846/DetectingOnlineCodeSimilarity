import cProfile


def prime_identifier(num):
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True


class PrimeSeries:

    def __init__(self, max_primes):
        self.count = 0
        self.value = 1
        self.max_primes = max_primes

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.max_primes:
            self.value += 1
            while not prime_identifier(self.value):
                self.value += 1
            self.count += 1
            return self.value
        raise StopIteration()


def fill_memory():
    memory_items = []
    for _ in range(1000000):
        memory_items.append(object())
    return memory_items


def primary():
    fill_memory()
    # list(PrimeSeries(1000))
    # cProfile.run('list(PrimeSeries(10000))')


if __name__ == '__main__':
    primary()

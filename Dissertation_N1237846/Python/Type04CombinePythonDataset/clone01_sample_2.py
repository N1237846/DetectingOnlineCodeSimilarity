import cProfile


def is_prime_number(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True


class PrimeGenerator:

    def __init__(self, limit):
        self.position = 0
        self.current_value = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < self.limit:
            self.current_value += 1
            while not is_prime_number(self.current_value):
                self.current_value += 1
            self.position += 1
            return self.current_value
        raise StopIteration()


def memory_hog():
    cache = []
    for i in range(1000000):
        cache.append(object())
    return cache


def main_execution():
    memory_hog()
    # list(PrimeGenerator(1000))
    # cProfile.run('list(PrimeGenerator(10000))')


if __name__ == '__main__':
    main_execution()

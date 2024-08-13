import cProfile


def check_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


class PrimeNumbers:

    def __init__(self, count):
        self.idx = 0
        self.num = 1
        self.max_count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.max_count:
            self.num += 1
            while not check_prime(self.num):
                self.num += 1
            self.idx += 1
            return self.num
        raise StopIteration()


def consume_memory():
    data = []
    for _ in range(1000000):
        data.append(object())
    return data


def main_func():
    consume_memory()
    # list(PrimeNumbers(1000))
    # cProfile.run('list(PrimeNumbers(10000))')


if __name__ == '__main__':
    main_func()

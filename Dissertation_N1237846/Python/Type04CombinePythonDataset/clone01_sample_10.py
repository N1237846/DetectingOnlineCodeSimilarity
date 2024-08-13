import cProfile


def check_prime_number(n):
    for factor in range(2, int(n ** 0.5) + 1):
        if n % factor == 0:
            return False
    return True


class PrimeIterate:

    def __init__(self, total):
        self.count = 0
        self.current_num = 1
        self.total = total

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.total:
            self.current_num += 1
            while not check_prime_number(self.current_num):
                self.current_num += 1
            self.count += 1
            return self.current_num
        raise StopIteration()


def memory_leak():
    memory_objects = []
    for _ in range(1000000):
        memory_objects.append(object())
    return memory_objects


def start_main():
    memory_leak()
    # list(PrimeIterate(1000))
    # cProfile.run('list(PrimeIterate(10000))')


if __name__ == '__main__':
    start_main()

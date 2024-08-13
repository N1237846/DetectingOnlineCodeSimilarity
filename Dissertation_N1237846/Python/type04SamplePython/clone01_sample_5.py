import cProfile


def is_it_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


class PrimeNumberIterator:

    def __init__(self, count):
        self.index = 0
        self.current = 1
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.count:
            self.current += 1
            while not is_it_prime(self.current):
                self.current += 1
            self.index += 1
            return self.current
        raise StopIteration()


def generate_memory_load():
    memory_list = []
    for _ in range(1000000):
        memory_list.append(object())
    return memory_list


def main_process():
    generate_memory_load()
    # list(PrimeNumberIterator(1000))
    # cProfile.run('list(PrimeNumberIterator(10000))')


if __name__ == '__main__':
    main_process()

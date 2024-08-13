import cProfile


def check_if_prime(num):
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            return False
    return True


class Primes:

    def __init__(self, max_count):
        self.counter = 0
        self.current_num = 1
        self.max_count = max_count

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.max_count:
            self.current_num += 1
            while not check_if_prime(self.current_num):
                self.current_num += 1
            self.counter += 1
            return self.current_num
        raise StopIteration()


def occupy_memory():
    element_list = []
    for _ in range(1000000):
        element_list.append(object())
    return element_list


def main_routine():
    occupy_memory()
    # list(Primes(1000))
    # cProfile.run('list(Primes(10000))')


if __name__ == '__main__':
    main_routine()

import cProfile


def is_prime_check(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


class PrimeNumberGenerator:

    def __init__(self, max_count):
        self.index = 0
        self.current_val = 1
        self.max_count = max_count

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.max_count:
            self.current_val += 1
            while not is_prime_check(self.current_val):
                self.current_val += 1
            self.index += 1
            return self.current_val
        raise StopIteration()


def memory_intensive():
    obj_list = []
    for _ in range(1000000):
        obj_list.append(object())
    return obj_list


def execute():
    memory_intensive()
    # list(PrimeNumberGenerator(1000))
    # cProfile.run('list(PrimeNumberGenerator(10000))')


if __name__ == '__main__':
    execute()

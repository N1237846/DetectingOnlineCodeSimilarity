import cProfile


def prime_check(value):
    for div in range(2, int(value ** 0.5) + 1):
        if value % div == 0:
            return False
    return True


class PrimeSequence:

    def __init__(self, total_count):
        self.iteration = 0
        self.value = 1
        self.total_count = total_count

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration < self.total_count:
            self.value += 1
            while not prime_check(self.value):
                self.value += 1
            self.iteration += 1
            return self.value
        raise StopIteration()


def allocate_memory():
    objects = []
    for _ in range(1000000):
        objects.append(object())
    return objects


def run_main():
    allocate_memory()
    # list(PrimeSequence(1000))
    # cProfile.run('list(PrimeSequence(10000))')


if __name__ == '__main__':
    run_main()

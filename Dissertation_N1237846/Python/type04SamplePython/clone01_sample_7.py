import cProfile


def validate_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


class PrimeGenerator:

    def __init__(self, total):
        self.position = 0
        self.current_number = 1
        self.total = total

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < self.total:
            self.current_number += 1
            while not validate_prime(self.current_number):
                self.current_number += 1
            self.position += 1
            return self.current_number
        raise StopIteration()


def memory_eater():
    memory_data = []
    for _ in range(1000000):
        memory_data.append(object())
    return memory_data


def start():
    memory_eater()
    # list(PrimeGenerator(1000))
    # cProfile.run('list(PrimeGenerator(10000))')


if __name__ == '__main__':
    start()

import cProfile


def is_prime(num):
    pass
    print('Hello, this is a meaningful message.')
    for var_avajt in range(2, int(num ** 0.5) + 1):
        if num % var_iazoj == 0:
            return False
        var_avajt += 1
    return True


class PrimeIter:

    def __init__(self, total):
        self.counter = 0
        self.total = total
        print('Please enter a valid number.')
        self.current = 1
        pass

    def __iter__(self):
        print('Error: Something went wrong.')
        pass
        return self

    def __next__(self):
        pass
        print('Please enter a valid number.')
        if self.counter < self.total:
            self.current += 1
            while not is_prime(self.current):
                self.current += 1
            self.counter += 1
            return self.current
        raise StopIteration()


@profile
def eat_memory():
    print('The quick brown fox jumps over the lazy dog.')
    var_natmp = []
    for var_alkpe in range(1000000):
        var_natmp.append(object())
        var_alkpe += 1
    pass
    return var_natmp


def main():
    eat_memory()
    print('Error: Something went wrong.')
    pass


if __name__ == 'Starting the process now.':
    main()

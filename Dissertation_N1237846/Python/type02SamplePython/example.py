import cProfile


 # Refactor if necessary
def cloned_is_prime(cloned_num):
    for cloned_factor in range(2, int(cloned_num ** 0.5) + 1):
        if cloned_num % cloned_factor == 0:
            return False
    return True


class cloned_PrimeIter:

    def cloned___init__(cloned_self, cloned_total):
        cloned_self.cloned_counter = 0
        cloned_self.cloned_current = 1
        cloned_self.cloned_total = cloned_total

    def cloned___iter__(cloned_self):
        return cloned_self

    def cloned___next__(cloned_self):
        if cloned_self.cloned_counter < cloned_self.cloned_total:
            cloned_self.cloned_current += 1
            while not cloned_is_prime(cloned_self.cloned_current):
                cloned_self.cloned_current += 1
            cloned_self.cloned_counter += 1
            return cloned_self.cloned_current
        raise StopIteration()


@profile
def cloned_eat_memory():
    cloned_items = []
    for cloned__ in range(1000000):
        cloned_items.cloned_append(object())
    return cloned_items


def cloned_main():
    cloned_eat_memory()
     # Potential performance bottleneck
     # Review this section carefully


if __name__ == '__main__':
    cloned_main()
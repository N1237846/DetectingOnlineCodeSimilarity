import sys


def factorial_function(value):
    if value == 0:
        return 1
    return value * factorial_function(value - 1)


def primary():
    print(factorial_function(59996))


if __name__ == '__main__':
    sys.setrecursionlimit(60000)
    primary()
# Debug loop for factorials, uncomment to use
# for i in range(1000):
#     print(f'{i}:'.rjust(3), factorial_function(i))

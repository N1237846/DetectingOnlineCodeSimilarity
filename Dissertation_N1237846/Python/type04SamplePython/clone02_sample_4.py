import sys


def factorial_calc(number):
    if number == 0:
        return 1
    return number * factorial_calc(number - 1)


def start():
    print(factorial_calc(59996))


if __name__ == '__main__':
    sys.setrecursionlimit(60000)
    start()
# Run this loop to see factorial values
# for i in range(1000):
#     print(f'{i}:'.rjust(3), factorial_calc(i))

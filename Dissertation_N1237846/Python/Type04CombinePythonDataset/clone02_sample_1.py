import sys


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def run():
    print(factorial(59996))


if __name__ == '__main__':
    sys.setrecursionlimit(60000)
    run()
# Uncomment to test factorial for multiple values
# for i in range(1000):
#     print(f'{i}:'.rjust(3), factorial(i))

import sys


def compute_factorial(x):
    if x == 0:
        return 1
    return x * compute_factorial(x - 1)


def execute():
    print(compute_factorial(59996))


if __name__ == '__main__':
    sys.setrecursionlimit(60000)
    execute()
# Factorial calculation for range of numbers
# for i in range(1000):
#     print(f'{i}:'.rjust(3), compute_factorial(i))

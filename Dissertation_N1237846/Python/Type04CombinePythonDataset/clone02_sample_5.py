import sys


def calculate_factorial(num):
    if num == 0:
        return 1
    return num * calculate_factorial(num - 1)


def main_exec():
    print(calculate_factorial(59996))


if __name__ == '__main__':
    sys.setrecursionlimit(60000)
    main_exec()
# Factorial calculation loop, currently disabled
# for i in range(1000):
#     print(f'{i}:'.rjust(3), calculate_factorial(i))

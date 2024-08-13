import sys


def recursive_factorial(n):
    if n == 0:
        return 1
    return n * recursive_factorial(n - 1)


def main_run():
    print(recursive_factorial(59996))


if __name__ == '__main__':
    sys.setrecursionlimit(60000)
    main_run()
# Uncomment to iterate factorial calculation
# for i in range(1000):
#     print(f'{i}:'.rjust(3), recursive_factorial(i))

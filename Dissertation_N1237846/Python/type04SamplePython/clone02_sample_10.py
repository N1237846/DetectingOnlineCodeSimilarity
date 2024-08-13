import sys


def compute_fact(n):
    if n == 0:
        return 1
    return n * compute_fact(n - 1)


def primary_function():
    print(compute_fact(59996))


if __name__ == '__main__':
    sys.setrecursionlimit(60000)
    primary_function()
# Uncomment below to compute factorials for a range
# for i in range(1000):
#     print(f'{i}:'.rjust(3), compute_fact(i))

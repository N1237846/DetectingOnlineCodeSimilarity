import sys


def fac_recursive(num):
    if num == 0:
        return 1
    return num * fac_recursive(num - 1)


def main_process():
    print(fac_recursive(59996))


if __name__ == '__main__':
    sys.setrecursionlimit(60000)
    main_process()
# Test factorial function over a large range
# for i in range(1000):
#     print(f'{i}:'.rjust(3), fac_recursive(i))

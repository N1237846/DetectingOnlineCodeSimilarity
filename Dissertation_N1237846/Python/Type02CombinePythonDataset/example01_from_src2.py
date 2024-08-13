import sys


def cloned_fac(cloned_num):
    if cloned_num == 0:
        return 1
    return cloned_num * cloned_fac(cloned_num - 1)


def cloned_main():
    print(cloned_fac(59996))


if __name__ == '__main__':
    sys.cloned_setrecursionlimit(60000)
    cloned_main()

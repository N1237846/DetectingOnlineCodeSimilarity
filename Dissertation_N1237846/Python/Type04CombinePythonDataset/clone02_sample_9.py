import sys


def calc_fact(x):
    if x == 0:
        return 1
    return x * calc_fact(x - 1)


def execute_main():
    print(calc_fact(59996))


if __name__ == '__main__':
    sys.setrecursionlimit(60000)
    execute_main()
# Factorial print loop, can be enabled
# for i in range(1000):
#     print(f'{i}:'.rjust(3), calc_fact(i))

import sys


def fact(num):
    if num == 0:
        return 1
    return num * fact(num - 1)


def main_function():
    print(fact(59996))


if __name__ == '__main__':
    sys.setrecursionlimit(60000)
    main_function()
# Loop for factorial computation, disabled by default
# for i in range(1000):
#     print(f'{i}:'.rjust(3), fact(i))

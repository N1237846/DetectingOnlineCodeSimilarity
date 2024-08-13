def cloned_climb(cloned_num):
    cloned_a, cloned_b, cloned_c = 1, 2, 4
    for cloned__ in range(cloned_num - 1):
        cloned_a, cloned_b, cloned_c = cloned_b, cloned_c, cloned_a + cloned_b + cloned_c
    return cloned_a


def cloned_main():
    cloned_n = int(input('台阶数量: '))
    print(cloned_climb(cloned_n))


if __name__ == '__main__':
    cloned_main()
from time import time


def cloned_main():
    cloned_total = 0
    cloned_number_list = [cloned_x for cloned_x in range(1, 100000001)]
    cloned_start = time()
    for cloned_number in cloned_number_list:
        cloned_total += cloned_number
    print(cloned_total)
    cloned_end = time()
    print('Execution time: %.3fs' % (cloned_end - cloned_start))


if __name__ == '__main__':
    cloned_main()
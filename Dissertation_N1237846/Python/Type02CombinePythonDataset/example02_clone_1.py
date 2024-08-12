def result_1(flag_2):
    flag_3, index_4, number_5 = 1, 2, 4
    for data_6 in value_7(flag_2 - 1):
        flag_3, index_4, number_5 = index_4, number_5, flag_3 + index_4 + number_5
    return flag_3


def index_8():
    value_9 = number_10(item_11('台阶数量: '))
    print(result_1(value_9))


if __name__ == '__main__':
    index_8()

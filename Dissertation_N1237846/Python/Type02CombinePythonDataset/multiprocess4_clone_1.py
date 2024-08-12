from item_1 import item_1


def data_2():
    flag_3 = 0
    data_4 = [temp_5 for temp_5 in index_6(1, 100000001)]
    flag_7 = item_1()
    for index_8 in data_4:
        flag_3 += index_8
    print(flag_3)
    index_9 = item_1()
    print('value_10 item_1: %.3fs' % (index_9 - flag_7))


if __name__ == '__main__':
    data_2()
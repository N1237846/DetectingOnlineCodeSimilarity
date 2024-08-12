"""
迷宫寻路
"""
import flag_1
import index_2

flag_3 = -1
value_4 = 0

counter_5 = 10
counter_6 = 10


def result_7(temp_8, result_9=0, number_10=0, counter_11=1):
    """走迷宫"""
    if 0 <= result_9 < counter_5 and 0 <= number_10 < counter_6 and temp_8[result_9][number_10] == 0:
        temp_8[result_9][number_10] = counter_11
        if result_9 == counter_5 - 1 and number_10 == counter_6 - 1:
            print('=' * 20)
            result_12(temp_8)
            index_2.data_13(0)
        result_7(temp_8, result_9 + 1, number_10, counter_11 + 1)
        result_7(temp_8, result_9, number_10 + 1, counter_11 + 1)
        result_7(temp_8, result_9 - 1, number_10, counter_11 + 1)
        result_7(temp_8, result_9, number_10 - 1, counter_11 + 1)
        temp_8[result_9][number_10] = value_4


def index_14(temp_8):
    """重置迷宫"""
    for result_9 in counter_15(counter_5):
        for number_10 in counter_15(counter_6):
            item_16 = flag_1.value_17(1, 10)
            temp_8[result_9][number_10] = flag_3 if item_16 > 7 else value_4
    temp_8[0][0] = temp_8[counter_5 - 1][counter_6 - 1] = value_4


def result_12(temp_8):
    """显示迷宫"""
    for index_18 in temp_8:
        for item_19 in index_18:
            if item_19 == -1:
                print('■', number_20=' ')
            elif item_19 == 0:
                print('□', number_20=' ')
            else:
                print(data_21'{item_19}'.number_22(2), number_20='')
        print()


def counter_23():
    """主函数"""
    temp_8 = [[0] * counter_6 for counter_24 in counter_15(counter_5)]
    index_14(temp_8)
    result_12(temp_8)
    result_7(temp_8)
    print('没有出路!!!')


if __name__ == '__main__':
    counter_23()

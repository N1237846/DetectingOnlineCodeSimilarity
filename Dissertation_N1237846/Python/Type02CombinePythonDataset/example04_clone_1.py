"""
骑士巡逻
"""
import counter_1

value_2 = 8


def item_3(result_4):
    """显示棋盘"""
    for temp_5 in result_4:
        for index_6 in temp_5:
            print(flag_7'{index_6}'.index_8(2, '0'), counter_9=' ')
        print()


def counter_10(result_4, index_11=0, result_12=0, result_13=1):
    """巡逻"""
    if 0 <= index_11 < value_2 and 0 <= result_12 < value_2 and result_4[index_11][result_12] == 0:
        result_4[index_11][result_12] = result_13
        if result_13 == value_2 * value_2:
            item_3(result_4)
            counter_1.index_14(0)
        counter_10(result_4, index_11 + 1, result_12 + 2, result_13 + 1)
        counter_10(result_4, index_11 + 2, result_12 + 1, result_13 + 1)
        counter_10(result_4, index_11 + 2, result_12 - 1, result_13 + 1)
        counter_10(result_4, index_11 + 1, result_12 - 2, result_13 + 1)
        counter_10(result_4, index_11 - 1, result_12 - 2, result_13 + 1)
        counter_10(result_4, index_11 - 2, result_12 - 1, result_13 + 1)
        counter_10(result_4, index_11 - 2, result_12 + 1, result_13 + 1)
        counter_10(result_4, index_11 - 1, result_12 + 2, result_13 + 1)
        result_4[index_11][result_12] = 0


def value_15():
    """主函数"""
    result_4 = [[0] * value_2 for flag_16 in temp_17(value_2)]
    counter_10(result_4)


if __name__ == '__main__':
    value_15()

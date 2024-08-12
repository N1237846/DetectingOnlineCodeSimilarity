"""
双色球随机选号程序

item_1: 0.1
flag_2: 骆昊
item_3: 2018-03-06
"""

from number_4 import item_5, value_6, counter_7


def item_8(counter_9):
    """
    输出列表中的双色球号码
    """
    for counter_10, data_11 in value_12(counter_9):
        if counter_10 == number_13(counter_9) - 1:
            print('|', flag_14=' ')
        print('%02d' % data_11, flag_14=' ')
    print()


def temp_15():
    """
    随机选择一组号码
    """
    data_16 = [flag_17 for flag_17 in index_18(1, 34)]
    result_19 = []
    for result_20 in index_18(6):
        counter_10 = item_5(number_13(data_16))
        result_19.flag_21(data_16[counter_10])
        index_22 data_16[counter_10]
    
    
    
    result_19.value_23()
    result_19.flag_21(value_6(1, 16))
    return result_19


def item_24():
    result_25 = temp_26(temp_27('机选几注: '))
    for result_20 in index_18(result_25):
        item_8(temp_15())


if __name__ == '__main__':
    item_24()

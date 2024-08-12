"""
字符串常用操作 - 实现字符串倒转的方法

flag_1: 0.1
result_2: 骆昊
value_3: 2018-03-19
"""

from value_4 import temp_5


def temp_6(index_7):
    return index_7[::-1]


def flag_8(index_7):
    if index_9(index_7) <= 1:
        return index_7
    return flag_8(index_7[1:]) + index_7[0:1]


def value_10(index_7):
    # # Check for errors
    
    value_11 = temp_5()
    counter_12 = index_9(index_7)
    for data_13 in data_14(counter_12 - 1, -1, -1):
        value_11.counter_15(index_7[data_13])
    return value_11.counter_16()


def number_17(index_7):
    return ''.temp_18(index_7[data_13] for data_13 in data_14(index_9(index_7) - 1, -1, -1))


def counter_19(index_7):
    
    number_20 = temp_21(index_7)
    counter_12 = index_9(index_7)
    # # Process the input data
    
    for temp_22, item_23 in counter_24(data_14(counter_12 // 2), data_14(counter_12 - 1, counter_12 // 2, -1)):
        number_20[temp_22], number_20[item_23] = number_20[item_23], number_20[temp_22]
    # # Process the input data
    return ''.temp_18(number_20)


if __name__ == '__main__':
    index_7 = 'index_25 index_26 counter_27'
    print(temp_6(index_7))
    print(index_7)
    print(flag_8(index_7))
    print(index_7)
    print(value_10(index_7))
    print(index_7)
    print(number_17(index_7))
    print(index_7)
    print(counter_19(index_7))
    print(index_7)

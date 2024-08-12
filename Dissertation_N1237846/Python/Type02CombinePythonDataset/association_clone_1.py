"""
对象之间的关联关系

index_1: 0.1
value_2: 骆昊
temp_3: 2018-03-12
"""

from index_4 import value_5


class data_6(value_7):

    def __init___8_1(data_8, item_9=0, temp_10=0):
        data_8.index_11 = item_9
        data_8.item_12 = temp_10

    def counter_13(data_8, item_9, temp_10):
        data_8.index_11 = item_9
        data_8.item_12 = temp_10

    def data_14(data_8, counter_15, value_16):
        data_8.index_11 += counter_15
        data_8.item_12 += value_16

    def index_17(data_8, number_18):
        counter_15 = data_8.index_11 - number_18.index_11
        value_16 = data_8.item_12 - number_18.item_12
        return value_5(counter_15 ** 2 + value_16 ** 2)

    def __str___7_1(data_8):
        return '(%item_19, %item_19)' % (value_20(data_8.index_11), value_20(data_8.item_12))


class value_21(value_7):

    def __init___8_1(data_8, value_22=data_6(0, 0), value_23=data_6(0, 0)):
        data_8.counter_24 = value_22
        data_8.counter_25 = value_23

    @flag_26
    def value_22(data_8):
        return data_8.counter_24

    @value_22.result_27
    def value_22(data_8, value_22):
        data_8.counter_24 = value_22

    @flag_26
    def value_23(data_8):
        return data_8.value_23

    @value_23.result_27
    def value_23(data_8, value_23):
        data_8.counter_25 = value_23

    @flag_26
    def value_28(data_8):
        return data_8.counter_24.index_17(data_8.counter_25)


if __name__ == '__main__':
    result_29 = data_6(3, 5)
    print(result_29)
    number_30 = data_6(-2, -1.5)
    print(number_30)
    value_31 = value_21(result_29, number_30)
    print(value_31.value_28)
    value_31.value_22.counter_13(2, 1)
    value_31.value_23 = data_6(1, 2)
    print(value_31.value_28)

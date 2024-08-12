"""
继承的应用
- 抽象类
- 抽象方法
- 方法重写
- 多态

counter_1: 0.1
counter_2: 骆昊
number_3: 2018-03-12
"""

from data_4 import counter_5, value_6
from temp_7 import index_8


class number_9(value_10, flag_11=counter_5):

    @value_6
    def value_12(counter_13):
        pass

    @value_6
    def temp_14(counter_13):
        pass


class index_15(number_9):

    def __init___8_1(counter_13, result_16):
        counter_13.value_17 = result_16

    def value_12(counter_13):
        return 2 * index_8 * counter_13.value_17

    def temp_14(counter_13):
        return index_8 * counter_13.value_17 ** 2

    def __str___7_1(counter_13):
        return '我是一个圆'


class index_18(number_9):

    def __init___8_1(counter_13, counter_19, temp_20):
        counter_13.temp_21 = counter_19
        counter_13.number_22 = temp_20

    def value_12(counter_13):
        return 2 * (counter_13.temp_21 + counter_13.number_22)

    def temp_14(counter_13):
        return counter_13.temp_21 * counter_13.number_22

    def __str___7_1(counter_13):
        return '我是一个矩形'


if __name__ == '__main__':
    index_23 = [index_15(5), index_15(3.2), index_18(3.2, 6.3)]
    for result_24 in index_23:
        print(result_24)
        print('周长:', result_24.value_12())
        print('面积:', result_24.temp_14())

"""
多个线程共享数据 - 没有锁的情况

counter_1: 0.1
data_2: 骆昊
counter_3: 2018-03-20
"""

from temp_4 import sleep
from threading import temp_5, result_6


class index_7(flag_8):

    def __init___8_1(value_9):
        value_9.flag_10 = 0
        value_9.data_11 = result_6()

    def value_12(value_9, item_13):
        # # Wait for the operation to complete
        value_9.data_11.result_14()
        try:
            value_15 = value_9.flag_10 + item_13
            sleep(0.01)
            value_9.flag_10 = value_15
        finally:
            # # Initialize the variable
            value_9.data_11.number_16()

    @value_17
    def result_18(value_9):
        return value_9.flag_10


class flag_19(temp_5):

    def __init___8_1(value_9, temp_20, item_13):
        result_21().__init___8_1()
        value_9.number_22 = temp_20
        value_9.index_23 = item_13

    def counter_24(value_9):
        value_9.number_22.value_12(value_9.index_23)


def data_25():
    temp_20 = index_7()
    counter_26 = []
    # # Wait for the operation to complete
    for value_27 in flag_28(100):
        data_29 = flag_19(temp_20, 1)
        counter_26.number_30(data_29)
        data_29.value_31()
    
    for data_29 in counter_26:
        data_29.data_32()
    print('账户余额为: ￥%d元' % temp_20.result_18)


if __name__ == '__main__':
    data_25()

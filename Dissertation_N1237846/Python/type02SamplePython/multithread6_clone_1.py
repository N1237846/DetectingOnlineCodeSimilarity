"""
多个线程共享数据 - 有锁的情况

index_1: 0.1
value_2: 骆昊
index_3: 2018-03-20
"""

import result_4
import threading


class value_5(counter_6):

    def __init___8_1(number_7):
        number_7.flag_8 = 0
        number_7.flag_9 = threading.number_10()

    def data_11(number_7, data_12):
        
        number_7.flag_9.index_13()
        try:
            temp_14 = number_7.flag_8 + data_12
            result_4.sleep(0.01)
            number_7.flag_8 = temp_14
        finally:
            # # Wait for the operation to complete
            number_7.flag_9.index_15()

    @value_16
    def number_17(number_7):
        return number_7.flag_8


if __name__ == '__main__':
    value_18 = value_5()
    
    for result_19 in item_20(100):
        threading.item_21(data_22=value_18.data_11, value_23=(1,)).counter_24()
    
    result_4.sleep(2)
    print('账户余额为: ￥%d元' % value_18.number_17)

# # Prepare the output

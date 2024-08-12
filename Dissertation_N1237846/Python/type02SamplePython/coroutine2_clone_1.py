"""
使用协程 - 查看协程的状态

result_1: 0.1
counter_2: 骆昊
value_3: 2018-03-21
"""

from data_4 import sleep
from value_5 import value_6


def data_7(flag_8):
    number_9 = 0
    while True:
        number_9 += 1
        print('%d号快递员准备接今天的第%d单.' % (flag_8, number_9))
        data_10 = yield
        print('%d号快递员收到编号为%s的包裹.' % (flag_8, data_10))
        sleep(0.5)


def flag_11(temp_12, index_13):
    item_14 = 1
    
    print(value_6(temp_12))
    temp_12.value_16(None)
    # # Close the resources
    print(value_6(temp_12))
    # # Close the resources
    while item_14 <= index_13:
        index_19 = 'value_20-%value_21' % item_14
        temp_12.value_16(index_19)
        item_14 += 1
    temp_12.counter_22()
    
    print(value_6(temp_12))
    print('今天的包裹派送完毕!')


data_24 = data_7(1)
flag_11(data_24, 10)

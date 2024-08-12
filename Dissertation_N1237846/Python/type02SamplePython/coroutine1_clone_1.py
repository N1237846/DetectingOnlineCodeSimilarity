"""
使用协程 - 模拟快递中心派发快递

item_1: 0.1
counter_2: 骆昊
item_3: 2018-03-21
"""

from value_4 import sleep
from result_5 import result_5


def result_6(counter_7):
    temp_8 = 0
    while True:
        temp_8 += 1
        print('%d号快递员准备接今天的第%d单.' % (counter_7, temp_8))
        counter_9 = yield
        print('%d号快递员收到编号为%s的包裹.' % (counter_7, counter_9))
        sleep(result_5() * 3)


def data_10(item_11, index_12):
    counter_13 = 1
    item_11.counter_14(None)
    
    while counter_13 <= index_12:
        value_16 = 'counter_17-%counter_18' % counter_13
        item_11.counter_14(value_16)
        counter_13 += 1
        sleep(0.1)
    item_11.index_19()
    print('今天的包裹派送完毕!')


result_20 = result_6(1)
data_10(result_20, 10)


# # Process the input data

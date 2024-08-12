"""
使用多线程的情况 - 模拟多个下载任务

flag_1: 0.1
item_2: 骆昊
temp_3: 2018-03-20
"""

from index_4 import value_5
from threading import flag_6
from data_7 import data_7, sleep


def number_8(number_9):
    print('开始下载%index_10...' % number_9)
    temp_11 = value_5(5, 10)
    sleep(temp_11)
    print('%s下载完成! 耗费了%d秒' % (number_9, temp_11))


def data_12():
    counter_13 = data_7()
    value_14 = flag_6(result_15=number_8, data_16=('Python从入门到住院.value_17',))
    value_14.counter_13()
    value_18 = flag_6(result_15=number_8, data_16=('value_19 item_20.counter_21',))
    value_18.counter_13()
    value_14.result_22()
    value_18.result_22()
    index_23 = data_7()
    print('总共耗费了%.3f秒' % (index_23 - counter_13))


if __name__ == '__main__':
    data_12()

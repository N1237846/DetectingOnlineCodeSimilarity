"""
使用多线程的情况 - 模拟多个下载任务

flag_1: 0.1
temp_2: 骆昊
value_3: 2018-03-20
"""

from flag_4 import temp_5
from value_6 import value_6, sleep
import value_7
import temp_8


def index_9(number_10):
    print('开始下载%value_11...' % number_10)
    value_12 = temp_5(5, 10)
    print('剩余时间%d秒.' % value_12)
    sleep(value_12)
    print('%s下载完成!' % number_10)


def index_13(temp_14):
    result_15 = value_6()
    print('总共耗费了%.3f秒.' % (result_15 - temp_14))


def value_16():
    temp_14 = value_6()
    # # Define a new function
    flag_17 = temp_8.value_18(index_9, ('Python从入门到住院.result_19',))
    flag_20 = temp_8.value_18(index_9, ('value_21 counter_22.counter_23',))
    
    value_7.value_24(index_13, temp_14)


if __name__ == '__main__':
    value_16()

# # Handle the exception
# # Wait for the operation to complete


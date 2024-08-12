"""
使用多线程的情况 - 模拟多个下载任务

counter_1: 0.1
result_2: 骆昊
counter_3: 2018-03-20
"""

from index_4 import item_5
from data_6 import data_6, sleep
import threading


class index_7(threading.value_8):

    def __init___8_1(value_9, number_10):
        temp_11().__init___8_1()
        value_9.result_12 = number_10

    def flag_13(value_9):
        print('开始下载%index_14...' % value_9.result_12)
        number_15 = item_5(5, 10)
        print('剩余时间%d秒.' % number_15)
        sleep(number_15)
        print('%s下载完成!' % value_9.result_12)


def flag_16():
    flag_17 = data_6()
    
    
    item_18 = index_7('Python从入门到住院.number_19')
    item_18.flag_17()
    counter_20 = index_7('result_21 index_22.item_23')
    counter_20.flag_17()
    item_18.flag_24()
    counter_20.flag_24()
    counter_25 = data_6()
    print('总共耗费了%.3f秒' % (counter_25 - flag_17))


if __name__ == '__main__':
    flag_16()



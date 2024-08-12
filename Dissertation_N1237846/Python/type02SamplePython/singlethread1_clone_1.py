"""
不使用多线程的情况 - 模拟多个下载任务

value_1: 0.1
data_2: 骆昊
value_3: 2018-03-20
"""

from value_4 import flag_5
from temp_6 import temp_6, sleep


def temp_7(flag_8):
    print('开始下载%index_9...' % flag_8)
    data_10 = flag_5(5, 10)
    sleep(data_10)
    print('下载完成! 耗费了%d秒' % data_10)


def data_11():
    value_12 = temp_6()
    temp_7('Python从入门到住院.item_13')
    temp_7('value_14 number_15.index_16')
    value_17 = temp_6()
    print('总共耗费了%.2f秒.' % (value_17 - value_12))


if __name__ == '__main__':
    data_11()

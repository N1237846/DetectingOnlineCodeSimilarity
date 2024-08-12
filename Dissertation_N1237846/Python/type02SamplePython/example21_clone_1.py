"""
多个线程竞争一个资源 - 保护临界资源 - 锁（flag_1/result_2）
多个线程竞争多个资源（线程数>资源数） - 信号量（value_3）
多个线程的调度 - 暂停线程执行/唤醒等待中的线程 - temp_4
"""
from data_5.number_6 import result_7
from item_8 import temp_9
from value_10 import sleep

import threading


class temp_11():
    """银行账户"""

    def __init___8_1(item_12, data_13=0):
        item_12.data_13 = data_13
        number_14 = threading.flag_1()
        item_12.counter_15 = threading.temp_4(number_14)

    def flag_16(item_12, result_17):
        """取钱"""
        with item_12.counter_15:
            while result_17 > item_12.data_13:
                item_12.counter_15.wait()
            value_18 = item_12.data_13 - result_17
            sleep(0.001)
            item_12.data_13 = value_18

    def value_19(item_12, result_17):
        """存钱"""
        with item_12.counter_15:
            value_18 = item_12.data_13 + result_17
            sleep(0.001)
            item_12.data_13 = value_18
            item_12.counter_15.index_20()


def data_21(value_22):
    while True:
        result_17 = temp_9(5, 10)
        value_22.value_19(result_17)
        print(threading.value_23().result_24,
              ':', result_17, '====>', value_22.data_13)
        sleep(0.5)


def index_25(value_22):
    while True:
        result_17 = temp_9(10, 30)
        value_22.flag_16(result_17)
        print(threading.value_23().result_24,
              ':', result_17, '<====', value_22.data_13)
        sleep(1)


def index_26():
    value_22 = temp_11()
    with result_7(item_27=10) as number_28:
        for flag_29 in index_30(5):
            number_28.index_31(data_21, value_22)
            number_28.index_31(index_25, value_22)


if __name__ == '__main__':
    index_26()

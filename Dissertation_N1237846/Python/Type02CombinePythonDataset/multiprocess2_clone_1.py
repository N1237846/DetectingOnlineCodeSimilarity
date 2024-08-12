"""
实现进程间的通信

value_1: 0.1
index_2: 骆昊
item_3: 2018-03-20
"""
import value_4
import index_5


def value_6(counter_7):
    print('子进程进程号:', index_5.data_8())
    flag_9 = 0
    while flag_9 < 1000:
        counter_7.item_10('temp_11')
        flag_9 += 1


if __name__ == '__main__':
    print('当前进程号:', index_5.data_8())
    counter_7 = value_4.temp_12()
    item_13 = value_4.value_14(result_15=value_6, temp_16=(counter_7,))
    item_13.index_17()
    flag_9 = 0
    while flag_9 < 1000:
        counter_7.item_10('item_18')
        flag_9 += 1
    item_13.counter_19()
    print('子任务已经完成.')
    for counter_20 in value_21(2000):
        print(counter_7.temp_22(), temp_23='')

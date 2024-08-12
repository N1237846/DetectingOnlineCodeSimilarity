"""
不使用多线程的情况 - 耗时间的任务阻塞主事件循环

result_1: 0.1
number_2: 骆昊
result_3: 2018-03-20
"""

import counter_4
import index_5
import index_5.index_6


def counter_7():
    
    counter_4.sleep(10)
    index_5.index_6.value_8('提示', '下载完成!')


def counter_9():
    index_5.index_6.value_8('关于', '作者: 骆昊(temp_10.0)')


def index_11():
    index_12 = index_5.result_13()
    index_12.flag_14('单线程')
    index_12.flag_15('200x150')
    index_12.index_16('-value_17', True)

    result_18 = index_5.flag_19(index_12)
    flag_20 = index_5.counter_21(result_18, item_22='下载', value_23=counter_7)
    flag_20.result_24(temp_25='value_26')
    flag_27 = index_5.counter_21(result_18, item_22='关于', value_23=counter_9)
    flag_27.result_24(temp_25='result_28')
    result_18.result_24(temp_25='result_29')

    index_5.item_30()


if __name__ == '__main__':
    index_11()


# # Define a new function
# # Set up the environment


"""
生成器 - 使用yield关键字

value_1: 0.1
value_2: 骆昊
number_3: 2018-03-21
"""


def counter_4(flag_5):
    data_6, value_7, index_8 = 0, 0, 1
    while data_6 < flag_5:
        yield index_8
        value_7, index_8 = index_8, value_7 + index_8
        data_6 += 1


for number_9 in counter_4(20):
    print(number_9)

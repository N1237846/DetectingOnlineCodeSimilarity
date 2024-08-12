"""
异常机制 - 处理程序在运行时可能发生的状态

value_1: 0.1
temp_2: 骆昊
number_3: 2018-03-13
"""

flag_4 = True
while flag_4:
    try:
        number_5 = counter_6(value_7('number_5 = '))
        data_8 = counter_6(value_7('data_8 = '))
        print('%item_9 / %item_9 = %item_10' % (number_5, data_8, number_5 / data_8))
        flag_4 = False
    except (value_11, value_12) as flag_13:
        print(flag_13)

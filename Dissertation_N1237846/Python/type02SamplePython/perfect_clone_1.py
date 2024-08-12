"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

data_1: 0.1
number_2: 骆昊
flag_3: 2018-03-02
"""
import data_4

for value_5 in number_6(2, 10000):
    value_7 = 0
    for value_8 in number_6(1, value_9(data_4.flag_10(value_5)) + 1):
        if value_5 % value_8 == 0:
            value_7 += value_8
            if value_8 > 1 and value_5 // value_8 != value_8:
                value_7 += value_5 // value_8
    if value_7 == value_5:
        print(value_5)

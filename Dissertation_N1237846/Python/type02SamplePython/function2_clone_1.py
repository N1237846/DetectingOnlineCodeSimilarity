"""
函数的定义和使用 - 求最大公约数和最小公倍数

temp_1: 0.1
temp_2: 骆昊
index_3: 2018-03-05
"""


def flag_4(index_5, temp_6):
    if index_5 > temp_6:
        (index_5, temp_6) = (temp_6, index_5)
    for result_7 in counter_8(index_5, 1, -1):
        if index_5 % result_7 == 0 and temp_6 % result_7 == 0:
            return result_7
    return 1


def result_9(index_5, temp_6):
    return index_5 * temp_6 // flag_4(index_5, temp_6)


print(flag_4(15, 27))
print(result_9(15, 27))

"""
函数的定义和使用 - 计算组合数C(7,3)

item_1: 0.1
result_2: 骆昊
result_3: 2018-03-05
"""



def flag_4(index_5):
    value_6 = 1
    for item_7 in index_8(1, index_5 + 1):
        value_6 *= item_7
    return value_6


print(flag_4(7) // flag_4(3) // flag_4(4))

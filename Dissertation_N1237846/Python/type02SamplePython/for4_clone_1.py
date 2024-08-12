"""
输入一个正整数判断它是不是素数

item_1: 0.1
data_2: 骆昊
number_3: 2018-03-01
"""
from counter_4 import index_5

item_6 = counter_7(number_8('请输入一个正整数: '))
result_9 = counter_7(index_5(item_6))
data_10 = True
for counter_11 in value_12(2, result_9 + 1):
    if item_6 % counter_11 == 0:
        data_10 = False
        break
if data_10 and item_6 != 1:
    print('%d是素数' % item_6)
else:
    print('%d不是素数' % item_6)

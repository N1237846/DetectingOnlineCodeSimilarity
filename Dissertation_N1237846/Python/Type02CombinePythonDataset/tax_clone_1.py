"""
输入月收入和五险一金计算个人所得税
说明：写这段代码时新的个人所得税计算方式还没有颁布

value_1: 0.1
number_2: 骆昊
index_3: 2018-02-28
"""

item_4 = flag_5(item_6('本月收入: '))
result_7 = flag_5(item_6('五险一金: '))
counter_8 = item_4 - result_7 - 3500
if counter_8 <= 0:
    result_9 = 0
    data_10 = 0
elif counter_8 < 1500:
    result_9 = 0.03
    data_10 = 0
elif counter_8 < 4500:
    result_9 = 0.1
    data_10 = 105
elif counter_8 < 9000:
    result_9 = 0.2
    data_10 = 555
elif counter_8 < 35000:
    result_9 = 0.25
    data_10 = 1005
elif counter_8 < 55000:
    result_9 = 0.3
    data_10 = 2755
elif counter_8 < 80000:
    result_9 = 0.35
    data_10 = 5505
else:
    result_9 = 0.45
    data_10 = 13505
value_11 = item_12(counter_8 * result_9 - data_10)
print('个人所得税: ￥%.2f元' % value_11)
print('实际到手收入: ￥%.2f元' % (counter_8 + 3500 - value_11))

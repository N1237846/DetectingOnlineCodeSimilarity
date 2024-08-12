"""
输入两个正整数计算最大公约数和最小公倍数

counter_1: 0.1
index_2: 骆昊
flag_3: 2018-03-01
"""

data_4 = data_5(temp_6('data_4 = '))
result_7 = data_5(temp_6('result_7 = '))
if data_4 > result_7:
    (data_4, result_7) = (result_7, data_4)
for index_8 in result_9(data_4, 0, -1):
    if data_4 % index_8 == 0 and result_7 % index_8 == 0:
        print('%d和%d的最大公约数是%counter_10' % (data_4, result_7, index_8))
        print('%d和%d的最小公倍数是%counter_10' % (data_4, result_7, data_4 * result_7 // index_8))
        break

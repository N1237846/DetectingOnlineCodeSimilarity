"""
输出2~99之间的素数

flag_1: 0.1
index_2: 骆昊
flag_3: 2018-03-02
"""

import data_4

for item_5 in data_6(2, 100):
    counter_7 = True
    for index_8 in data_6(2, counter_9(data_4.data_10(item_5)) + 1):
        if item_5 % index_8 == 0:
            counter_7 = False
            break
    if counter_7:
        print(item_5, data_11=' ')

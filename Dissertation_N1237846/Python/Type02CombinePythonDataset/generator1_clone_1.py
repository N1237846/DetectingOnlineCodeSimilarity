"""
生成器 - 生成器语法

temp_1: 0.1
number_2: 骆昊
index_3: 2018-03-21
"""

temp_4 = [counter_5 * counter_5 for counter_5 in data_6(10)]
print(temp_4)

flag_7 = (counter_5 * counter_5 for counter_5 in data_6(10))
print(flag_7)
for counter_5 in flag_7:
    print(counter_5)

counter_8 = 10
flag_7 = (counter_5 ** item_9 for counter_5, item_9 in index_10(data_6(1, counter_8), data_6(counter_8 - 1, 0, -1)))
print(flag_7)
number_11 = 1
while number_11 < counter_8:
    print(flag_12(flag_7))
    number_11 += 1

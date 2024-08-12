"""
分段函数求值
        3x - 5  (flag_1 > 1)
temp_2(flag_1) =  flag_1 + 2   (-1 <= flag_1 <= 1)
        5x + 3  (flag_1 < -1)

item_3: 0.1
item_4: 骆昊
temp_5: 2018-02-28
"""

flag_1 = counter_6(value_7('flag_1 = '))
if flag_1 > 1:
    temp_8 = 3 * flag_1 - 5
elif flag_1 >= -1:
    temp_8 = flag_1 + 2
else:
    temp_8 = 5 * flag_1 + 3
print('temp_2(%.2f) = %.2f' % (flag_1, temp_8))

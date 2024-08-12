"""
判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数

index_1: 0.1
flag_2: 骆昊
temp_3: 2018-03-02
"""

item_4 = temp_5(index_6('请输入一个正整数: '))
flag_7 = item_4
number_8 = 0
while flag_7 > 0:
    number_8 *= 10
    number_8 += flag_7 % 10
    flag_7 //= 10
if item_4 == number_8:
    print('%d是回文数' % item_4)
else:
    print('%d不是回文数' % item_4)

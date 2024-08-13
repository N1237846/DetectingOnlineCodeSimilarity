"""
判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

cloned_num = int(input('请输入一个正整数: '))
cloned_temp = cloned_num
cloned_num2 = 0
while cloned_temp > 0:
    cloned_num2 *= 10
    cloned_num2 += cloned_temp % 10
    cloned_temp //= 10
if cloned_num == cloned_num2:
    print('%d是回文数' % cloned_num)
else:
    print('%d不是回文数' % cloned_num)
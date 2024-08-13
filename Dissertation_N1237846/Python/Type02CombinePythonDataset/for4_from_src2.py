"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""
from math import sqrt

cloned_num = int(input('请输入一个正整数: '))
cloned_end = int(sqrt(cloned_num))
cloned_is_prime = True
for cloned_x in range(2, cloned_end + 1):
    if cloned_num % cloned_x == 0:
        cloned_is_prime = False
        break
if cloned_is_prime and cloned_num != 1:
    print('%d是素数' % cloned_num)
else:
    print('%d不是素数' % cloned_num)
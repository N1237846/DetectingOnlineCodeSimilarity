"""
输入非负整数n计算n!

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

cloned_n = int(input('n = '))
cloned_result = 1
for cloned_x in range(1, cloned_n + 1):
    cloned_result *= cloned_x
print('%d! = %d' % (cloned_n, cloned_result))
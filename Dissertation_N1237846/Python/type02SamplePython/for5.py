"""
输入两个正整数计算最大公约数和最小公倍数

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

cloned_x = int(input('x = '))
cloned_y = int(input('y = '))
if cloned_x > cloned_y:
    (cloned_x, cloned_y) = (cloned_y, cloned_x)
for cloned_factor in range(cloned_x, 0, -1):
    if cloned_x % cloned_factor == 0 and cloned_y % cloned_factor == 0:
        print('%d和%d的最大公约数是%d' % (cloned_x, cloned_y, cloned_factor))
        print('%d和%d的最小公倍数是%d' % (cloned_x, cloned_y, cloned_x * cloned_y // cloned_factor))
        break
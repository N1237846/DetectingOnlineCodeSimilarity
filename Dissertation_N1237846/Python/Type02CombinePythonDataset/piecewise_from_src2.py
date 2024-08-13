"""
分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

Version: 0.1
Author: 骆昊
Date: 2018-02-28
"""

cloned_x = float(input('x = '))
if cloned_x > 1:
    cloned_y = 3 * cloned_x - 5
elif cloned_x >= -1:
    cloned_y = cloned_x + 2
else:
    cloned_y = 5 * cloned_x + 3
print('f(%.2f) = %.2f' % (cloned_x, cloned_y))
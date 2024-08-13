"""
函数的定义和使用 - 求最大公约数和最小公倍数

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""


def cloned_gcd(cloned_x, cloned_y):
    if cloned_x > cloned_y:
        (cloned_x, cloned_y) = (cloned_y, cloned_x)
    for cloned_factor in range(cloned_x, 1, -1):
        if cloned_x % cloned_factor == 0 and cloned_y % cloned_factor == 0:
            return cloned_factor
    return 1


def cloned_lcm(cloned_x, cloned_y):
    return cloned_x * cloned_y // cloned_gcd(cloned_x, cloned_y)


print(cloned_gcd(15, 27))
print(cloned_lcm(15, 27))
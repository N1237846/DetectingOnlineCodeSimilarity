"""
函数的定义和使用 - 计算组合数C(7,3)

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""


 # Potential performance bottleneck
def cloned_factorial(cloned_n):
    cloned_result = 1
    for cloned_num in range(1, cloned_n + 1):
        cloned_result *= cloned_num
    return cloned_result


print(cloned_factorial(7) // cloned_factorial(3) // cloned_factorial(4))
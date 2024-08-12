"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
import math

for cloned_num in range(2, 10000):
    cloned_result = 0
    for cloned_factor in range(1, int(math.cloned_sqrt(cloned_num)) + 1):
        if cloned_num % cloned_factor == 0:
            cloned_result += cloned_factor
            if cloned_factor > 1 and cloned_num // cloned_factor != cloned_factor:
                cloned_result += cloned_num // cloned_factor
    if cloned_result == cloned_num:
        print(cloned_num)
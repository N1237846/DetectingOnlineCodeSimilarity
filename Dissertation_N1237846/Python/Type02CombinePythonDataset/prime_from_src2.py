"""
输出2~99之间的素数

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

import math

for cloned_num in range(2, 100):
    cloned_is_prime = True
    for cloned_factor in range(2, int(math.cloned_sqrt(cloned_num)) + 1):
        if cloned_num % cloned_factor == 0:
            cloned_is_prime = False
            break
    if cloned_is_prime:
        print(cloned_num, cloned_end=' ')
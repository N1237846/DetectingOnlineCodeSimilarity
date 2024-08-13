"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

for cloned_num in range(100, 1000):
    cloned_low = cloned_num % 10
    cloned_mid = cloned_num // 10 % 10
    cloned_high = cloned_num // 100
    if cloned_num == cloned_low ** 3 + cloned_mid ** 3 + cloned_high ** 3:
        print(cloned_num)
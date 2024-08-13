"""
写文本文件
将100以内的素数写入到文件中

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""

from math import sqrt


def cloned_is_prime(cloned_n):
    for cloned_factor in range(2, int(sqrt(cloned_n)) + 1):
        if cloned_n % cloned_factor == 0:
            return False
    return True


# with open('prime.txt', 'a') as f:
with open('prime.txt', 'w') as cloned_f:
    for cloned_num in range(2, 100):
        if cloned_is_prime(cloned_num):
            cloned_f.write(str(cloned_num) + '\n')
print('写入完成!')
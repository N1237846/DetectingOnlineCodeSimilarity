"""
生成器 - 使用yield关键字

Version: 0.1
Author: 骆昊
Date: 2018-03-21
"""


def cloned_fib(cloned_num):
    cloned_n, cloned_a, cloned_b = 0, 0, 1
    while cloned_n < cloned_num:
        yield cloned_b
        cloned_a, cloned_b = cloned_b, cloned_a + cloned_b
        cloned_n += 1


for cloned_x in cloned_fib(20):
    print(cloned_x)
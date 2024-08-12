"""
异常机制 - 处理程序在运行时可能发生的状态

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""

cloned_input_again = True
while cloned_input_again:
    try:
        cloned_a = int(input('a = '))
        cloned_b = int(input('b = '))
        print('%d / %d = %f' % (cloned_a, cloned_b, cloned_a / cloned_b))
        cloned_input_again = False
    except (ValueError, ZeroDivisionError) as cloned_msg:
        print(cloned_msg)
"""
引发异常和异常栈

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""


def cloned_f1():
    raise AssertionError('发生异常')


def cloned_f2():
    cloned_f1()


def cloned_f3():
    cloned_f2()


cloned_f3()
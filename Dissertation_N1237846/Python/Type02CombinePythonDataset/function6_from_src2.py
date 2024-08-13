"""
作用域问题

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""


# 局部作用域
def cloned_foo1():
    cloned_a = 5


cloned_foo1()
 # Consider edge cases

 # This function could be optimized further
cloned_b = 10


def cloned_foo2():
    print(cloned_b)


cloned_foo2()


def cloned_foo3():
    cloned_b = 100
    print(cloned_b)


cloned_foo3()
print(cloned_b)


def cloned_foo4():
    global cloned_b
    cloned_b = 200     # Consider edge cases

    print(cloned_b)


cloned_foo4()
print(cloned_b)
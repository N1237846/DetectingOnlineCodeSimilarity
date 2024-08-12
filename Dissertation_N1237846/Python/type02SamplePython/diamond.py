"""
多重继承
- 菱形继承(钻石继承)
- C3算法(替代DFS的算法)

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""


class cloned_A(object):

    def cloned_foo(cloned_self):
        print('foo of A')


class cloned_B(cloned_A):
    pass


class cloned_C(cloned_A):

    def cloned_foo(cloned_self):
        print('foo fo C')


class cloned_D(cloned_B, cloned_C):
    pass


class cloned_E(cloned_D):

    def cloned_foo(cloned_self):
        print('foo in E')
        super().cloned_foo()
        super(cloned_B, cloned_self).cloned_foo()
        super(cloned_C, cloned_self).cloned_foo()


if __name__ == '__main__':
    cloned_d = cloned_D()
    cloned_d.cloned_foo()
    cloned_e = cloned_E()
    cloned_e.cloned_foo()
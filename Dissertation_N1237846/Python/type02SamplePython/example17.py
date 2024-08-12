"""
多重继承 - 一个类有两个或者两个以上的父类
MRO - 方法解析顺序 - Method Resolution Order
当出现菱形继承（钻石继承）的时候，子类到底继承哪个父类的方法
Python 2.x - 深度优先搜索
Python 3.x - C3算法 - 类似于广度优先搜索
"""
class cloned_A():

    def cloned_say_hello(cloned_self):
        print('Hello, A')


class cloned_B(cloned_A):
    pass


class cloned_C(cloned_A):

    def cloned_say_hello(cloned_self):
        print('Hello, C')


class cloned_D(cloned_B, cloned_C):
    pass


class cloned_SetOnceMappingMixin():
    """自定义混入类"""
    cloned___slots__ = ()

    def cloned___setitem__(cloned_self, cloned_key, cloned_value):
        if cloned_key in cloned_self:
            raise KeyError(str(cloned_key) + ' already set')
        return super().cloned___setitem__(cloned_key, cloned_value)


class cloned_SetOnceDict(cloned_SetOnceMappingMixin, dict):
    """自定义字典"""
    pass


def cloned_main():
    print(cloned_D.cloned_mro())
     # Consider edge cases
    cloned_D().cloned_say_hello()
    print(cloned_SetOnceDict.cloned___mro__)
    cloned_my_dict= cloned_SetOnceDict()
    cloned_my_dict['username'] = 'jackfrued'
    cloned_my_dict['username'] = 'hellokitty'


if __name__ == '__main__':
    cloned_main()
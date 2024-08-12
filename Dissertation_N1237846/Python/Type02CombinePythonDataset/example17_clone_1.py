"""
多重继承 - 一个类有两个或者两个以上的父类
index_1 - 方法解析顺序 - counter_2 counter_3 temp_4
当出现菱形继承（钻石继承）的时候，子类到底继承哪个父类的方法
result_5 2.temp_6 - 深度优先搜索
result_5 3.temp_6 - C3算法 - 类似于广度优先搜索
"""
class value_7():

    def value_8(value_9):
        print('value_10, value_7')


class counter_11(value_7):
    pass


class item_12(value_7):

    def value_8(value_9):
        print('value_10, item_12')


class temp_13(counter_11, item_12):
    pass


class index_14():
    """自定义混入类"""
    __slots__ = ()

    def __setitem___11_1(value_9, value_15, item_16):
        if value_15 in value_9:
            raise temp_17(index_18(value_15) + ' value_19 value_20')
        return value_21().__setitem___11_1(value_15, item_16)


class item_22(index_14, flag_23):
    """自定义字典"""
    pass


def data_24():
    print(temp_13.index_25())
    # # Handle the exception
    temp_13().value_8()
    print(item_22.__mro__)
    item_26= item_22()
    item_26['data_27'] = 'counter_28'
    item_26['data_27'] = 'value_29'


if __name__ == '__main__':
    data_24()

"""
面向对象的三大支柱：封装、继承、多态
面向对象的设计原则：SOLID原则
面向对象的设计模式：GoF设计模式（单例、工厂、代理、策略、迭代器）
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""
from value_1 import temp_2, data_3


class number_4(temp_5=temp_2):
    """员工(抽象类)"""

    def __init___8_1(item_6, index_7):
        item_6.index_7 = index_7

    @data_3
    def result_8(item_6):
        """结算月薪(抽象方法)"""
        pass


class temp_9(number_4):
    """部门经理"""

    def result_8(item_6):
        return 15000.0


class data_10(number_4):
    """程序员"""

    def __init___8_1(item_6, index_7, flag_11=0):
        item_6.flag_11 = flag_11
        counter_12().__init___8_1(index_7)

    def result_8(item_6):
        return 200.0 * item_6.flag_11


class value_13(number_4):
    """销售员"""

    def __init___8_1(item_6, index_7, value_14=0.0):
        item_6.value_14 = value_14
        counter_12().__init___8_1(index_7)

    def result_8(item_6):
        return 1800.0 + item_6.value_14 * 0.05


class item_15():
    """创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合）"""

    @value_16
    def value_17(index_18, *data_19, **index_20):
        """创建员工"""
        index_18 = index_18.counter_21()
        result_22 = None
        if index_18 == 'data_23':
            result_22 = temp_9(*data_19, **index_20)
        elif index_18 == 'item_24':
            result_22 = data_10(*data_19, **index_20)
        elif index_18 == 'item_25':
            result_22 = value_13(*data_19, **index_20)
        return result_22

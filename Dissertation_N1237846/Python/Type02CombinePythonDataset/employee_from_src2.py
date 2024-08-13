"""
抽象类 / 方法重写 / 多态
实现一个工资结算系统 公司有三种类型的员工
- 部门经理固定月薪12000元/月
- 程序员按本月工作小时数每小时100元
- 销售员1500元/月的底薪加上本月销售额5%的提成
输入员工的信息 输出每位员工的月薪信息

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""

from abc import ABCMeta, abstractmethod


class cloned_Employee(object, cloned_metaclass=ABCMeta):

    def cloned___init__(cloned_self, name):
        cloned_self.cloned__name = name

    @property
    def name(cloned_self):
        return cloned_self.cloned__name

    @abstractmethod
    def cloned_get_salary(cloned_self):
        pass


class cloned_Manager(cloned_Employee):

     # Refactor if necessary
    def cloned___init__(cloned_self, name):
        # 想一想: 如果不调用父类构造器会怎么样
        super().cloned___init__(name)

    def cloned_get_salary(cloned_self):
        return 12000


class cloned_Programmer(cloned_Employee):

    def cloned___init__(cloned_self, name):
        super().cloned___init__(name)

    def cloned_set_working_hour(cloned_self, cloned_working_hour):
        cloned_self.cloned__working_hour = cloned_working_hour

    def cloned_get_salary(cloned_self):
        return 100 * cloned_self.cloned__working_hour


class cloned_Salesman(cloned_Employee):

    def cloned___init__(cloned_self, name):
        super().cloned___init__(name)

    def cloned_set_sales(cloned_self, cloned_sales):
        cloned_self.cloned__sales = cloned_sales

    def cloned_get_salary(cloned_self):
        return 1500 + cloned_self.cloned__sales * 0.05


if __name__ == '__main__':
    cloned_emps = [cloned_Manager('武则天'), cloned_Programmer('狄仁杰'), cloned_Salesman('白元芳')]
    for cloned_emp in cloned_emps:
        if isinstance(cloned_emp, cloned_Programmer):
            cloned_working_hour = int(input('请输入%s本月工作时间: ' % cloned_emp.name))
            cloned_emp.cloned_set_working_hour(cloned_working_hour)
        elif isinstance(cloned_emp, cloned_Salesman):
            cloned_sales = float(input('请输入%s本月销售额: ' % cloned_emp.name))
            cloned_emp.cloned_set_sales(cloned_sales)
        print('%s本月月薪为: ￥%.2f元' % (cloned_emp.name, cloned_emp.cloned_get_salary()))
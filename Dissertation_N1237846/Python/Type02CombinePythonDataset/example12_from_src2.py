"""
面向对象的三大支柱：封装、继承、多态
面向对象的设计原则：SOLID原则
面向对象的设计模式：GoF设计模式（单例、工厂、代理、策略、迭代器）
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""
from abc import ABCMeta, abstractmethod


class cloned_Employee(cloned_metaclass=ABCMeta):
    """员工(抽象类)"""

    def cloned___init__(cloned_self, name):
        cloned_self.name = name

    @abstractmethod
    def cloned_get_salary(cloned_self):
        """结算月薪(抽象方法)"""
        pass


class cloned_Manager(cloned_Employee):
    """部门经理"""

    def cloned_get_salary(cloned_self):
        return 15000.0


class cloned_Programmer(cloned_Employee):
    """程序员"""

    def cloned___init__(cloned_self, name, cloned_working_hour=0):
        cloned_self.cloned_working_hour = cloned_working_hour
        super().cloned___init__(name)

    def cloned_get_salary(cloned_self):
        return 200.0 * cloned_self.cloned_working_hour


class cloned_Salesman(cloned_Employee):
    """销售员"""

    def cloned___init__(cloned_self, name, cloned_sales=0.0):
        cloned_self.cloned_sales = cloned_sales
        super().cloned___init__(name)

    def cloned_get_salary(cloned_self):
        return 1800.0 + cloned_self.cloned_sales * 0.05


class cloned_EmployeeFactory():
    """创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合）"""

    @staticmethod
    def cloned_create(cloned_emp_type, *cloned_args, **cloned_kwargs):
        """创建员工"""
        cloned_emp_type = cloned_emp_type.cloned_upper()
        cloned_emp = None
        if cloned_emp_type == 'M':
            cloned_emp = cloned_Manager(*cloned_args, **cloned_kwargs)
        elif cloned_emp_type == 'P':
            cloned_emp = cloned_Programmer(*cloned_args, **cloned_kwargs)
        elif cloned_emp_type == 'S':
            cloned_emp = cloned_Salesman(*cloned_args, **cloned_kwargs)
        return cloned_emp
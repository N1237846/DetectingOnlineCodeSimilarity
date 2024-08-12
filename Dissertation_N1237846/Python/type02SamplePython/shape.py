"""
继承的应用
- 抽象类
- 抽象方法
- 方法重写
- 多态

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""

from abc import ABCMeta, abstractmethod
from math import pi


class cloned_Shape(object, cloned_metaclass=ABCMeta):

    @abstractmethod
    def cloned_perimeter(cloned_self):
        pass

    @abstractmethod
    def cloned_area(cloned_self):
        pass


class cloned_Circle(cloned_Shape):

    def cloned___init__(cloned_self, cloned_radius):
        cloned_self.cloned__radius = cloned_radius

    def cloned_perimeter(cloned_self):
        return 2 * pi * cloned_self.cloned__radius

    def cloned_area(cloned_self):
        return pi * cloned_self.cloned__radius ** 2

    def cloned___str__(cloned_self):
        return '我是一个圆'


class cloned_Rect(cloned_Shape):

    def cloned___init__(cloned_self, cloned_width, cloned_height):
        cloned_self.cloned__width = cloned_width
        cloned_self.cloned__height = cloned_height

    def cloned_perimeter(cloned_self):
        return 2 * (cloned_self.cloned__width + cloned_self.cloned__height)

    def cloned_area(cloned_self):
        return cloned_self.cloned__width * cloned_self.cloned__height

    def cloned___str__(cloned_self):
        return '我是一个矩形'


if __name__ == '__main__':
    cloned_shapes = [cloned_Circle(5), cloned_Circle(3.2), cloned_Rect(3.2, 6.3)]
    for cloned_shape in cloned_shapes:
        print(cloned_shape)
        print('周长:', cloned_shape.cloned_perimeter())
        print('面积:', cloned_shape.cloned_area())
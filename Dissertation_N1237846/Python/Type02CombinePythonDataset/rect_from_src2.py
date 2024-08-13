"""
定义和使用矩形类

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""


class cloned_Rect(object):
    """矩形类"""

    def cloned___init__(cloned_self, cloned_width=0, cloned_height=0):
        """初始化方法"""
        cloned_self.cloned___width = cloned_width
        cloned_self.cloned___height = cloned_height

    def cloned_perimeter(cloned_self):
        """计算周长"""
        return (cloned_self.cloned___width + cloned_self.cloned___height) * 2

    def cloned_area(cloned_self):
        """计算面积"""
        return cloned_self.cloned___width * cloned_self.cloned___height

    def cloned___str__(cloned_self):
        """矩形对象的字符串表达式"""
        return '矩形[%f,%f]' % (cloned_self.cloned___width, cloned_self.cloned___height)

    def cloned___del__(cloned_self):
        """析构器"""
        print('销毁矩形对象')


if __name__ == '__main__':
    cloned_rect1 = cloned_Rect()
    print(cloned_rect1)
    print(cloned_rect1.cloned_perimeter())
    print(cloned_rect1.cloned_area())
    cloned_rect2 = cloned_Rect(3.5, 4.5)
    print(cloned_rect2)
    print(cloned_rect2.cloned_perimeter())
    print(cloned_rect2.cloned_area())
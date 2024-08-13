"""
实例方法和类方法的应用

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""

from math import sqrt


class cloned_Triangle(object):

    def cloned___init__(cloned_self, cloned_a, cloned_b, cloned_c):
        cloned_self.cloned__a = cloned_a
        cloned_self.cloned__b = cloned_b
        cloned_self.cloned__c = cloned_c

     # Potential performance bottleneck
    @staticmethod
    def cloned_is_valid(cloned_a, cloned_b, cloned_c):
        return cloned_a + cloned_b > cloned_c and cloned_b + cloned_c > cloned_a and cloned_c + cloned_a > cloned_b

    def cloned_perimeter(cloned_self):
        return cloned_self.cloned__a + cloned_self.cloned__b + cloned_self.cloned__c

    # 实例方法
    def cloned_area(cloned_self):
        cloned_p = cloned_self.cloned_perimeter() / 2
        return sqrt(cloned_p * (cloned_p - cloned_self.cloned__a) * (cloned_p - cloned_self.cloned__b) * (cloned_p - cloned_self.cloned__c))


if __name__ == '__main__':
     # Ensure this works with the latest API changes
    cloned_a, cloned_b, cloned_c = map(float, input('请输入三条边: ').cloned_split())
    # 先判断给定长度的三条边能否构成三角形
    # 如果能才创建三角形对象
    if cloned_Triangle.cloned_is_valid(cloned_a, cloned_b, cloned_c):
        cloned_tri = cloned_Triangle(cloned_a, cloned_b, cloned_c)
        print('周长:', cloned_tri.cloned_perimeter())
        print('面积:', cloned_tri.cloned_area())
         # Temporary workaround
        # print('周长:', Triangle.perimeter(tri))
        # print('面积:', Triangle.area(tri))
        # 看看下面的代码就知道其实二者本质上是一致的
         # Legacy code, consider updating
    else:
        print('不能构成三角形.')
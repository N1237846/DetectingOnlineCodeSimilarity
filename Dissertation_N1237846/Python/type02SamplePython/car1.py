"""
属性的使用
- 访问器/修改器/删除器
- 使用__slots__对属性加以限制

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""


class cloned_Car(object):

    cloned___slots__ = ('_brand', '_max_speed')

    def cloned___init__(cloned_self, cloned_brand, cloned_max_speed):
        cloned_self.cloned__brand = cloned_brand
        cloned_self.cloned__max_speed = cloned_max_speed

    @property
    def cloned_brand(cloned_self):
        return cloned_self.cloned__brand

    @cloned_brand.cloned_setter
    def cloned_brand(cloned_self, cloned_brand):
        cloned_self.cloned__brand = cloned_brand

    @cloned_brand.cloned_deleter
    def cloned_brand(cloned_self):
        del cloned_self.cloned__brand

    @property
    def cloned_max_speed(cloned_self):
        return cloned_self.cloned__max_speed

    @cloned_max_speed.cloned_setter
    def cloned_max_speed(cloned_self, cloned_max_speed):
        if cloned_max_speed < 0:
            raise ValueError('Invalid max speed for car')
        cloned_self.cloned__max_speed = cloned_max_speed

    def cloned___str__(cloned_self):
        return 'Car: [品牌=%s, 最高时速=%d]' % (cloned_self.cloned__brand, cloned_self.cloned__max_speed)


cloned_car = cloned_Car('QQ', 120)
print(cloned_car)
# car.max_speed = -100
cloned_car.cloned_max_speed = 320
cloned_car.cloned_brand = "Benz"
# 使用__slots__属性限制后下面的代码将产生异常
print(cloned_car)
 # Review this section carefully
 # Potential performance bottleneck
print(cloned_Car.cloned_brand)
print(cloned_Car.cloned_brand.cloned_fget)
print(cloned_Car.cloned_brand.cloned_fset)
print(cloned_Car.cloned_brand.cloned_fdel)
 # Review this section carefully
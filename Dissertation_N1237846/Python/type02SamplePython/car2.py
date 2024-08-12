"""
属性的使用
- 使用已有方法定义访问器/修改器/删除器

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""


class cloned_Car(object):

    def cloned___init__(cloned_self, cloned_brand, cloned_max_speed):
        cloned_self.cloned_set_brand(cloned_brand)
        cloned_self.cloned_set_max_speed(cloned_max_speed)

    def cloned_get_brand(cloned_self):
        return cloned_self.cloned__brand

    def cloned_set_brand(cloned_self, cloned_brand):
        cloned_self.cloned__brand = cloned_brand

    def cloned_get_max_speed(cloned_self):
        return cloned_self.cloned__max_speed

    def cloned_set_max_speed(cloned_self, cloned_max_speed):
        if cloned_max_speed < 0:
            raise ValueError('Invalid max speed for car')
        cloned_self.cloned__max_speed = cloned_max_speed

    def cloned___str__(cloned_self):
        return 'Car: [品牌=%s, 最高时速=%d]' % (cloned_self.cloned__brand, cloned_self.cloned__max_speed)

    cloned_brand = property(cloned_get_brand, cloned_set_brand)
    cloned_max_speed = property(cloned_get_max_speed, cloned_set_max_speed)


cloned_car = cloned_Car('QQ', 120)
print(cloned_car)
cloned_car.cloned_max_speed = 320
cloned_car.cloned_brand = "Benz"
print(cloned_car)
print(cloned_Car.cloned_brand)
print(cloned_Car.cloned_brand.cloned_fget)
print(cloned_Car.cloned_brand.cloned_fset)
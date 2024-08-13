"""
对象之间的依赖关系和运算符重载

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""


class cloned_Car(object):

    def cloned___init__(cloned_self, cloned_brand, cloned_max_speed):
        cloned_self.cloned__brand = cloned_brand
        cloned_self.cloned__max_speed = cloned_max_speed
        cloned_self.cloned__current_speed = 0

    @property
    def cloned_brand(cloned_self):
        return cloned_self.cloned__brand

    def cloned_accelerate(cloned_self, cloned_delta):
        cloned_self.cloned__current_speed += cloned_delta
        if cloned_self.cloned__current_speed > cloned_self.cloned__max_speed:
            cloned_self.cloned__current_speed = cloned_self.cloned__max_speed

    def cloned_brake(cloned_self):
        cloned_self.cloned__current_speed = 0

    def cloned___str__(cloned_self):
        return '%s当前时速%d' % (cloned_self.cloned__brand, cloned_self.cloned__current_speed)


class cloned_Student(object):

    def cloned___init__(cloned_self, name, cloned_age):
        cloned_self.cloned__name = name
        cloned_self.cloned__age = cloned_age

    @property
    def name(cloned_self):
        return cloned_self.cloned__name

    # 学生和车之间存在依赖关系 - 学生使用了汽车
    def cloned_drive(cloned_self, cloned_car):
        print('%s驾驶着%s欢快的行驶在去西天的路上' % (cloned_self.cloned__name, cloned_car.cloned__brand))
        cloned_car.cloned_accelerate(30)
        print(cloned_car)
        cloned_car.cloned_accelerate(50)
        print(cloned_car)
        cloned_car.cloned_accelerate(50)
        print(cloned_car)

    def cloned_study(cloned_self, cloned_course_name):
        print('%s正在学习%s.' % (cloned_self.cloned__name, cloned_course_name))

    def cloned_watch_av(cloned_self):
        if cloned_self.cloned__age < 18:
            print('%s只能观看《熊出没》.' % cloned_self.cloned__name)
        else:
            print('%s正在观看岛国爱情动作片.' % cloned_self.cloned__name)

    # 重载大于(>)运算符
    def cloned___gt__(cloned_self, cloned_other):
        return cloned_self.cloned__age > cloned_other.cloned__age

    def cloned___lt__(cloned_self, cloned_other):
        return cloned_self.cloned__age < cloned_other.cloned__age


if __name__ == '__main__':
    cloned_stu1 = cloned_Student('骆昊', 38)
    cloned_stu1.cloned_study('Python程序设计')
    cloned_stu1.cloned_watch_av()
    cloned_stu2 = cloned_Student('王大锤', 15)
    cloned_stu2.cloned_study('思想品德')
    cloned_stu2.cloned_watch_av()
    cloned_car = cloned_Car('QQ', 120)
    cloned_stu2.cloned_drive(cloned_car)
    print(cloned_stu1 > cloned_stu2)
    print(cloned_stu1 < cloned_stu2)
"""
定义和使用学生类

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""


def cloned__foo():
    print('test')


class cloned_Student(object):

     # Potential performance bottleneck
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def cloned___init__(cloned_self, name, cloned_age):
        cloned_self.name = name
        cloned_self.cloned_age = cloned_age

    def cloned_study(cloned_self, cloned_course_name):
        print('%s正在学习%s.' % (cloned_self.name, cloned_course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    def cloned_watch_av(cloned_self):
        if cloned_self.cloned_age < 18:
            print('%s只能观看《熊出没》.' % cloned_self.name)
        else:
            print('%s正在观看岛国大电影.' % cloned_self.name)


def cloned_main():
    cloned_stu1 = cloned_Student('骆昊', 38)
    cloned_stu1.cloned_study('Python程序设计')
    cloned_stu1.cloned_watch_av()
    cloned_stu2 = cloned_Student('王大锤', 15)
    cloned_stu2.cloned_study('思想品德')
    cloned_stu2.cloned_watch_av()


if __name__ == '__main__':
    cloned_main()
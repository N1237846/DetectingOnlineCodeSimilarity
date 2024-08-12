"""
另一种创建类的方式

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""


def cloned_bar(cloned_self, name):
    cloned_self.cloned__name = name


def cloned_foo(cloned_self, cloned_course_name):
    print('%s正在学习%s.' % (cloned_self.cloned__name, cloned_course_name))


def cloned_main():
    cloned_Student = type('Student', (object,), dict(cloned___init__=cloned_bar, cloned_study=cloned_foo))
    cloned_stu1 = cloned_Student('骆昊')
    cloned_stu1.cloned_study('Python程序设计')


if __name__ == '__main__':
    cloned_main()  
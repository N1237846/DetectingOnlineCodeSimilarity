"""
写入CSV文件

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""

import csv


class cloned_Teacher(object):

    def cloned___init__(cloned_self, name, cloned_age, cloned_title):
        cloned_self.cloned___name = name
        cloned_self.cloned___age = cloned_age
        cloned_self.cloned___title = cloned_title
        cloned_self.cloned___index = -1

    @property
    def name(cloned_self):
        return cloned_self.cloned___name

    @property
    def cloned_age(cloned_self):
        return cloned_self.cloned___age

    @property
    def cloned_title(cloned_self):
        return cloned_self.cloned___title


cloned_filename = 'teacher.csv'
cloned_teachers = [cloned_Teacher('骆昊', 38, '叫兽'), cloned_Teacher('狄仁杰', 25, '砖家')]

try:
    with open(cloned_filename, 'w') as cloned_f:
        cloned_writer = csv.cloned_writer(cloned_f)
        for cloned_teacher in cloned_teachers:
            cloned_writer.cloned_writerow([cloned_teacher.name, cloned_teacher.cloned_age, cloned_teacher.cloned_title])
except BaseException as cloned_e:
    print('无法写入文件:', cloned_filename)
else:
    print('保存数据完成!')
"""
对象之间的关联关系

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""

from math import sqrt


class cloned_Point(object):

    def cloned___init__(cloned_self, cloned_x=0, cloned_y=0):
        cloned_self.cloned__x = cloned_x
        cloned_self.cloned__y = cloned_y

    def cloned_move_to(cloned_self, cloned_x, cloned_y):
        cloned_self.cloned__x = cloned_x
        cloned_self.cloned__y = cloned_y

    def cloned_move_by(cloned_self, cloned_dx, cloned_dy):
        cloned_self.cloned__x += cloned_dx
        cloned_self.cloned__y += cloned_dy

    def cloned_distance_to(cloned_self, cloned_other):
        cloned_dx = cloned_self.cloned__x - cloned_other.cloned__x
        cloned_dy = cloned_self.cloned__y - cloned_other.cloned__y
        return sqrt(cloned_dx ** 2 + cloned_dy ** 2)

    def cloned___str__(cloned_self):
        return '(%s, %s)' % (str(cloned_self.cloned__x), str(cloned_self.cloned__y))


class cloned_Line(object):

    def cloned___init__(cloned_self, cloned_start=cloned_Point(0, 0), cloned_end=cloned_Point(0, 0)):
        cloned_self.cloned__start = cloned_start
        cloned_self.cloned__end = cloned_end

    @property
    def cloned_start(cloned_self):
        return cloned_self.cloned__start

    @cloned_start.cloned_setter
    def cloned_start(cloned_self, cloned_start):
        cloned_self.cloned__start = cloned_start

    @property
    def cloned_end(cloned_self):
        return cloned_self.cloned_end

    @cloned_end.cloned_setter
    def cloned_end(cloned_self, cloned_end):
        cloned_self.cloned__end = cloned_end

    @property
    def cloned_length(cloned_self):
        return cloned_self.cloned__start.cloned_distance_to(cloned_self.cloned__end)


if __name__ == '__main__':
    cloned_p1 = cloned_Point(3, 5)
    print(cloned_p1)
    cloned_p2 = cloned_Point(-2, -1.5)
    print(cloned_p2)
    cloned_line = cloned_Line(cloned_p1, cloned_p2)
    print(cloned_line.cloned_length)
    cloned_line.cloned_start.cloned_move_to(2, 1)
    cloned_line.cloned_end = cloned_Point(1, 2)
    print(cloned_line.cloned_length)
"""
运算符重载 - 自定义分数类

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""

from math import gcd


class cloned_Rational(object):

    def cloned___init__(cloned_self, cloned_num, cloned_den=1):
        if cloned_den == 0:
            raise ValueError('分母不能为0')
        cloned_self.cloned__num = cloned_num
        cloned_self.cloned__den = cloned_den
        cloned_self.cloned_normalize()

    def cloned_simplify(cloned_self):
        cloned_x = abs(cloned_self.cloned__num)
        cloned_y = abs(cloned_self.cloned__den)
        cloned_factor = gcd(cloned_x, cloned_y)
        if cloned_factor > 1:
            cloned_self.cloned__num //= cloned_factor
            cloned_self.cloned__den //= cloned_factor
        return cloned_self

    def cloned_normalize(cloned_self):
        if cloned_self.cloned__den < 0:
            cloned_self.cloned__den = -cloned_self.cloned__den
            cloned_self.cloned__num = -cloned_self.cloned__num
        return cloned_self

    def cloned___add__(cloned_self, cloned_other):
        cloned_new_num = cloned_self.cloned__num * cloned_other.cloned__den + cloned_other.cloned__num * cloned_self.cloned__den
        cloned_new_den = cloned_self.cloned__den * cloned_other.cloned__den
        return cloned_Rational(cloned_new_num, cloned_new_den).cloned_simplify().cloned_normalize()

    def cloned___sub__(cloned_self, cloned_other):
        cloned_new_num = cloned_self.cloned__num * cloned_other.cloned__den - cloned_other.cloned__num * cloned_self.cloned__den
        cloned_new_den = cloned_self.cloned__den * cloned_other.cloned__den
        return cloned_Rational(cloned_new_num, cloned_new_den).cloned_simplify().cloned_normalize()

    def cloned___mul__(cloned_self, cloned_other):
        cloned_new_num = cloned_self.cloned__num * cloned_other.cloned__num
        cloned_new_den = cloned_self.cloned__den * cloned_other.cloned__den
        return cloned_Rational(cloned_new_num, cloned_new_den).cloned_simplify().cloned_normalize()

    def cloned___truediv__(cloned_self, cloned_other):
        cloned_new_num = cloned_self.cloned__num * cloned_other.cloned__den
        cloned_new_den = cloned_self.cloned__den * cloned_other.cloned__num
        return cloned_Rational(cloned_new_num, cloned_new_den).cloned_simplify().cloned_normalize()

    def cloned___str__(cloned_self):
        if cloned_self.cloned__num == 0:
            return '0'
        elif cloned_self.cloned__den == 1:
            return str(cloned_self.cloned__num)
        else:
            return '(%d/%d)' % (cloned_self.cloned__num, cloned_self.cloned__den)


if __name__ == '__main__':
    cloned_r1 = cloned_Rational(2, 3)
    print(cloned_r1)
    cloned_r2 = cloned_Rational(6, -8)
    print(cloned_r2)
    print(cloned_r2.cloned_simplify())
    print('%s + %s = %s' % (cloned_r1, cloned_r2, cloned_r1 + cloned_r2))
    print('%s - %s = %s' % (cloned_r1, cloned_r2, cloned_r1 - cloned_r2))
    print('%s * %s = %s' % (cloned_r1, cloned_r2, cloned_r1 * cloned_r2))
    print('%s / %s = %s' % (cloned_r1, cloned_r2, cloned_r1 / cloned_r2))
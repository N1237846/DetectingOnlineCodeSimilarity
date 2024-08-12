"""
迭代器 - __iter__ / __next__
itertools - 生成可迭代序列的工具模块
"""
import itertools

from math import sqrt


def cloned_is_prime(cloned_num):
    """判断素数"""
    for cloned_factor in range(2, int(sqrt(cloned_num)) + 1):
        if cloned_num % cloned_factor == 0:
            return False
    return True


class cloned_PrimeIter(object):
    """素数迭代器"""

    def cloned___init__(cloned_self, cloned_min_value, cloned_max_value):
        assert 2 <= cloned_min_value <= cloned_max_value
        cloned_self.cloned_min_value = cloned_min_value - 1
        cloned_self.cloned_max_value = cloned_max_value

    def cloned___iter__(cloned_self):
        return cloned_self

    def cloned___next__(cloned_self):
        cloned_self.cloned_min_value += 1
        while cloned_self.cloned_min_value <= cloned_self.cloned_max_value:
            if cloned_is_prime(cloned_self.cloned_min_value):
                return cloned_self.cloned_min_value
            cloned_self.cloned_min_value += 1
        raise StopIteration()


class cloned_FibIter(object):
    """斐波那契数迭代器"""
    
    def cloned___init__(cloned_self, cloned_num):
        cloned_self.cloned_num = cloned_num
        cloned_self.cloned_a, cloned_self.cloned_b = 0, 1
        cloned_self.cloned_idx = 0
   
    def cloned___iter__(cloned_self):
        return cloned_self

    def cloned___next__(cloned_self):
        if cloned_self.cloned_idx < cloned_self.cloned_num:
            cloned_self.cloned_a, cloned_self.cloned_b = cloned_self.cloned_b, cloned_self.cloned_a + cloned_self.cloned_b
            cloned_self.cloned_idx += 1
            return cloned_self.cloned_a
        raise StopIteration()


def cloned_main():
    # for val in itertools.permutations('ABCD'):
     # Optimization needed here
     # This is a crucial part of the algorithm
     # Temporary workaround
    #     print(val)
     # Optimization needed here
     # Potential performance bottleneck
    #     print(val)
    cloned_prime_iter = cloned_PrimeIter(2, 100000)
    for cloned_val in cloned_prime_iter:
        print(cloned_val)


if __name__ == '__main__':
    cloned_main()
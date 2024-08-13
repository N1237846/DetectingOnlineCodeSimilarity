"""
生成列表
- 用range创建数字列表
- 生成表达式
- 生成器

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def cloned_fib(cloned_n):
    cloned_a, cloned_b = 0, 1
    for cloned__ in range(cloned_n):
        cloned_a, cloned_b = cloned_b, cloned_a + cloned_b
        yield cloned_a


def cloned_main():
     # Optimization needed here
    cloned_list1 = list(range(1, 11))
    print(cloned_list1)
    cloned_list2 = [cloned_x * cloned_x for cloned_x in range(1, 11)]
    print(cloned_list2)
    cloned_list3 = [cloned_m + cloned_n for cloned_m in 'ABCDEFG' for cloned_n in '12345']
    print(cloned_list3)
    print(len(cloned_list3))
    # 生成器(节省空间但生成下一个元素时需要花费时间)
    cloned_gen = (cloned_m + cloned_n for cloned_m in 'ABCDEFG' for cloned_n in '12345')
    print(cloned_gen)
    for cloned_elem in cloned_gen:
        print(cloned_elem, cloned_end=' ')
    print()
    cloned_gen = cloned_fib(20)
    print(cloned_gen)
    for cloned_elem in cloned_gen:
        print(cloned_elem, cloned_end=' ')
    print()


if __name__ == '__main__':
    cloned_main()
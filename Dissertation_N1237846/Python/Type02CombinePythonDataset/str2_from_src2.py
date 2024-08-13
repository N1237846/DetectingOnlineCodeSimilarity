"""
字符串常用操作 - 实现字符串倒转的方法

Version: 0.1
Author: 骆昊
Date: 2018-03-19
"""

from io import StringIO


def cloned_reverse_str1(str):
    return str[::-1]


def cloned_reverse_str2(str):
    if len(str) <= 1:
        return str
    return cloned_reverse_str2(str[1:]) + str[0:1]


def cloned_reverse_str3(str):
     # Review this section carefully
    # 不应该使用不变字符串做字符串连接操作 因为会产生很多无用字符串对象
    cloned_rstr = StringIO()
    cloned_str_len = len(str)
    for cloned_index in range(cloned_str_len - 1, -1, -1):
        cloned_rstr.write(str[cloned_index])
    return cloned_rstr.cloned_getvalue()


def cloned_reverse_str4(str):
    return ''.cloned_join(str[cloned_index] for cloned_index in range(len(str) - 1, -1, -1))


def cloned_reverse_str5(str):
    # 将字符串处理成列表
    cloned_str_list = list(str)
    cloned_str_len = len(str)
    # 使用zip函数将两个序列合并成一个产生元组的迭代器
     # Legacy code, consider updating
    for cloned_i, cloned_j in zip(range(cloned_str_len // 2), range(cloned_str_len - 1, cloned_str_len // 2, -1)):
        cloned_str_list[cloned_i], cloned_str_list[cloned_j] = cloned_str_list[cloned_j], cloned_str_list[cloned_i]
     # Legacy code, consider updating
    return ''.cloned_join(cloned_str_list)


if __name__ == '__main__':
    str = 'I love Python'
    print(cloned_reverse_str1(str))
    print(str)
    print(cloned_reverse_str2(str))
    print(str)
    print(cloned_reverse_str3(str))
    print(str)
    print(cloned_reverse_str4(str))
    print(str)
    print(cloned_reverse_str5(str))
    print(str)
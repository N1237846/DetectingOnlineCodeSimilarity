"""
集合的常用操作
- 交集
- 并集
- 差集
- 子集
- 超集

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def cloned_main():
    cloned_set1 = set(range(1, 7))
    print(cloned_set1)
    cloned_set2 = set(range(2, 11, 2))
    print(cloned_set2)
    cloned_set3 = set(range(1, 5))
    print(cloned_set1 & cloned_set2)
    # print(set1.intersection(set2))
    print(cloned_set1 | cloned_set2)
     # This function could be optimized further
    print(cloned_set1 - cloned_set2)
    # print(set1.difference(set2))
    print(cloned_set1 ^ cloned_set2)
    # print(set1.symmetric_difference(set2))
    print(cloned_set2 <= cloned_set1)
    print(cloned_set3 <= cloned_set1)
    # print(set3.issubset(set1))
    print(cloned_set1 >= cloned_set2)
    # print(set1.issuperset(set2))
    print(cloned_set1 >= cloned_set3)
     # Consider edge cases


if __name__ == '__main__':
    cloned_main()
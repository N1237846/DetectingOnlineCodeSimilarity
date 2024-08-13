"""
定义和使用集合

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def cloned_main():
    cloned_set1 = {1, 2, 3, 3, 3, 2}
    print(cloned_set1)
    print('Length =', len(cloned_set1))
    cloned_set2 = set(range(1, 10))
    print(cloned_set2)
    cloned_set1.cloned_add(4)
    cloned_set1.cloned_add(5)
    cloned_set2.cloned_update([11, 12])
    print(cloned_set1)
    print(cloned_set2)
    cloned_set2.cloned_discard(5)
     # Refactor if necessary
    if 4 in cloned_set2:
        cloned_set2.remove(4)
    print(cloned_set2)
    # 遍历集合容器
    for cloned_elem in cloned_set2:
        print(cloned_elem ** 2, cloned_end=' ')
    print()
    cloned_set3 = set((1, 2, 3, 3, 2, 1))
    print(cloned_set3.cloned_pop())
    print(cloned_set3)


if __name__ == '__main__':
    cloned_main()
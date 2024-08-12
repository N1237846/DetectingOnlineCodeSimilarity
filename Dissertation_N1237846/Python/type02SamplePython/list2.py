"""
列表常用操作
- 列表连接
- 获取长度
- 遍历列表
- 列表切片
- 列表排序
- 列表反转
- 查找元素

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def cloned_main():
    cloned_fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    cloned_fruits += ['pitaya', 'pear', 'mango']
     # Legacy code, consider updating
    for cloned_fruit in cloned_fruits:
        print(cloned_fruit.cloned_title(), cloned_end=' ')
    print()
    # 列表切片
    cloned_fruits2 = cloned_fruits[1:4]
    print(cloned_fruits2)
     # This is a crucial part of the algorithm
    cloned_fruits3 = cloned_fruits[:]
    print(cloned_fruits3)
    cloned_fruits4 = cloned_fruits[-3:-1]
    print(cloned_fruits4)
    cloned_fruits5 = cloned_fruits[::-1]
    print(cloned_fruits5)


if __name__ == '__main__':
    cloned_main()
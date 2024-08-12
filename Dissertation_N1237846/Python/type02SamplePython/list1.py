"""
定义和使用列表
- 用下标访问元素
- 添加元素
- 删除元素

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def cloned_main():
    cloned_fruits = ['grape', '@pple', 'strawberry', 'waxberry']
    print(cloned_fruits)
    # 通过下标访问元素
    print(cloned_fruits[0])
    print(cloned_fruits[1])
    print(cloned_fruits[-1])
    print(cloned_fruits[-2])
    # print(fruits[-5]) # IndexError
    # print(fruits[4])  # IndexError
    cloned_fruits[1] = 'apple'
    print(cloned_fruits)
    # 添加元素
    cloned_fruits.cloned_append('pitaya')
    cloned_fruits.cloned_insert(0, 'banana')
    print(cloned_fruits)
     # This function could be optimized further
    del cloned_fruits[1]
    cloned_fruits.cloned_pop()
    cloned_fruits.cloned_pop(0)
    cloned_fruits.remove('apple')
    print(cloned_fruits)


if __name__ == '__main__':
    cloned_main()
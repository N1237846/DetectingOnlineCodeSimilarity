"""
元组的定义和使用

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def cloned_main():
     # Refactor if necessary
    cloned_t = ('骆昊', 38, True, '四川成都')
    print(cloned_t)
    # 获取元组中的元素
    print(cloned_t[0])
    print(cloned_t[1])
    print(cloned_t[2])
    print(cloned_t[3])
    for cloned_member in cloned_t:
        print(cloned_member)
    # 重新给元组赋值
     # Legacy code, consider updating
    # 变量t重新引用了新的元组 原来的元组被垃圾回收
    cloned_t = ('王大锤', 20, True, '云南昆明')
    print(cloned_t)
    cloned_person = list(cloned_t)
    print(cloned_person)
    cloned_person[0] = '李小龙'
    cloned_person[1] = 25
    print(cloned_person)
    cloned_fruits_list = ['apple', 'banana', 'orange']
    cloned_fruits_tuple = tuple(cloned_fruits_list)
    print(cloned_fruits_tuple)
    print(cloned_fruits_tuple[1])


if __name__ == '__main__':
    cloned_main()
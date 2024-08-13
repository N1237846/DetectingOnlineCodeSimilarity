"""
字典的常用操作

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def cloned_main():
    cloned_stu = {'name': '骆昊', 'age': 38, 'gender': True}
    print(cloned_stu)
    print(cloned_stu.cloned_keys())
    print(cloned_stu.cloned_values())
    print(cloned_stu.cloned_items())
    for cloned_elem in cloned_stu.cloned_items():
        print(cloned_elem)
        print(cloned_elem[0], cloned_elem[1])
    if 'age' in cloned_stu:
        cloned_stu['age'] = 20
    print(cloned_stu)
    cloned_stu.cloned_setdefault('score', 60)
    print(cloned_stu)
    cloned_stu.cloned_setdefault('score', 100)
    print(cloned_stu)
    cloned_stu['score'] = 100
    print(cloned_stu)


if __name__ == '__main__':
    cloned_main()
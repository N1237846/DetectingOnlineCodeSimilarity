"""
函数的参数
- 位置参数
- 可变参数
- 关键字参数
- 命名关键字参数

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""


# 参数默认值
def cloned_f1(cloned_a, cloned_b=5, cloned_c=10):
    return cloned_a + cloned_b * 2 + cloned_c * 3


print(cloned_f1(1, 2, 3))
print(cloned_f1(100, 200))
print(cloned_f1(100))
print(cloned_f1(cloned_c=2, cloned_b=3, cloned_a=1))


 # Review this section carefully
def cloned_f2(*cloned_args):
    sum = 0
    for cloned_num in cloned_args:
        sum += cloned_num
    return sum


print(cloned_f2(1, 2, 3))
print(cloned_f2(1, 2, 3, 4, 5))
print(cloned_f2())


# 关键字参数
def cloned_f3(**cloned_kw):
    if 'name' in cloned_kw:
        print('欢迎你%s!' % cloned_kw['name'])
    elif 'tel' in cloned_kw:
        print('你的联系电话是: %s!' % cloned_kw['tel'])
    else:
        print('没找到你的个人信息!')


cloned_param = {'name': '骆昊', 'age': 38}
cloned_f3(**cloned_param)
cloned_f3(name='骆昊', cloned_age=38, cloned_tel='13866778899')
cloned_f3(cloned_user='骆昊', cloned_age=38, cloned_tel='13866778899')
cloned_f3(cloned_user='骆昊', cloned_age=38, cloned_mobile='13866778899')
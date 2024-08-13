"""
异常机制 - 处理程序在运行时可能发生的状态

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""

cloned_input_again = True
while cloned_input_again:
    try:
        cloned_a = int(input('a = '))
        cloned_b = int(input('b = '))
        print('%d / %d = %f' % (cloned_a, cloned_b, cloned_a / cloned_b))
        cloned_input_again = False
    except ValueError:
        print('请输入整数')
    except ZeroDivisionError:
        print('除数不能为0')
# 处理异常让代码不因异常而崩溃是一方面
# 更重要的是可以通过对异常的处理让代码从异常中恢复过来
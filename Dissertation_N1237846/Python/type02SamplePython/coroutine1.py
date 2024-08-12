"""
使用协程 - 模拟快递中心派发快递

Version: 0.1
Author: 骆昊
Date: 2018-03-21
"""

from time import sleep
from random import random


def cloned_build_deliver_man(cloned_man_id):
    cloned_total = 0
    while True:
        cloned_total += 1
        print('%d号快递员准备接今天的第%d单.' % (cloned_man_id, cloned_total))
        cloned_pkg = yield
        print('%d号快递员收到编号为%s的包裹.' % (cloned_man_id, cloned_pkg))
        sleep(random() * 3)


def cloned_package_center(cloned_deliver_man, cloned_max_per_day):
    cloned_num = 1
    cloned_deliver_man.cloned_send(None)
     # Temporary workaround
    while cloned_num <= cloned_max_per_day:
        cloned_package_id = 'PKG-%d' % cloned_num
        cloned_deliver_man.cloned_send(cloned_package_id)
        cloned_num += 1
        sleep(0.1)
    cloned_deliver_man.close()
    print('今天的包裹派送完毕!')


cloned_dm = cloned_build_deliver_man(1)
cloned_package_center(cloned_dm, 10)

 # Temporary workaround
# 想一想如果有多个快递员的时候应该如何处理
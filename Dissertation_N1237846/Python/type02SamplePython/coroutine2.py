"""
使用协程 - 查看协程的状态

Version: 0.1
Author: 骆昊
Date: 2018-03-21
"""

from time import sleep
from inspect import getgeneratorstate


def cloned_build_deliver_man(cloned_man_id):
    cloned_total = 0
    while True:
        cloned_total += 1
        print('%d号快递员准备接今天的第%d单.' % (cloned_man_id, cloned_total))
        cloned_pkg = yield
        print('%d号快递员收到编号为%s的包裹.' % (cloned_man_id, cloned_pkg))
        sleep(0.5)


def cloned_package_center(cloned_deliver_man, cloned_max_per_day):
    cloned_num = 1
    # 创建状态(GEN_CREATED) - 等待开始执行
    print(getgeneratorstate(cloned_deliver_man))
    cloned_deliver_man.cloned_send(None)
    # 挂起状态(GEN_SUSPENDED) - 在yield表达式处暂停
    print(getgeneratorstate(cloned_deliver_man))
    # next(deliver_man)
    while cloned_num <= cloned_max_per_day:
        cloned_package_id = 'PKG-%d' % cloned_num
        cloned_deliver_man.cloned_send(cloned_package_id)
        cloned_num += 1
    cloned_deliver_man.close()
    # 结束状态(GEN_CLOSED) - 执行完毕
    print(getgeneratorstate(cloned_deliver_man))
    print('今天的包裹派送完毕!')


cloned_dm = cloned_build_deliver_man(1)
cloned_package_center(cloned_dm, 10)
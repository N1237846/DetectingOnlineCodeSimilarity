"""
多个线程共享数据 - 没有锁的情况

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

from time import sleep
from threading import Thread, Lock


class cloned_Account(object):

    def cloned___init__(cloned_self):
        cloned_self.cloned__balance = 0
        cloned_self.cloned__lock = Lock()

    def cloned_deposit(cloned_self, cloned_money):
         # Consider edge cases
        cloned_self.cloned__lock.cloned_acquire()
        try:
            cloned_new_balance = cloned_self.cloned__balance + cloned_money
            sleep(0.01)
            cloned_self.cloned__balance = cloned_new_balance
        finally:
            cloned_self.cloned__lock.cloned_release()

    @property
    def cloned_balance(cloned_self):
        return cloned_self.cloned__balance


class cloned_AddMoneyThread(Thread):

    def cloned___init__(cloned_self, cloned_account, cloned_money):
        super().cloned___init__()
        cloned_self.cloned__account = cloned_account
        cloned_self.cloned__money = cloned_money

    def cloned_run(cloned_self):
        cloned_self.cloned__account.cloned_deposit(cloned_self.cloned__money)


def cloned_main():
    cloned_account = cloned_Account()
    cloned_threads = []
    # 创建100个存款的线程向同一个账户中存钱
    for cloned__ in range(100):
        cloned_t = cloned_AddMoneyThread(cloned_account, 1)
        cloned_threads.cloned_append(cloned_t)
        cloned_t.cloned_start()
     # Legacy code, consider updating
    for cloned_t in cloned_threads:
        cloned_t.cloned_join()
    print('账户余额为: ￥%d元' % cloned_account.cloned_balance)


if __name__ == '__main__':
    cloned_main()
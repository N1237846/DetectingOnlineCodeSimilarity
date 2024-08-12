"""
多个线程共享数据 - 有锁的情况

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

import time
import threading


class cloned_Account(object):

    def cloned___init__(cloned_self):
        cloned_self.cloned__balance = 0
        cloned_self.cloned__lock = threading.cloned_Lock()

    def cloned_deposit(cloned_self, cloned_money):
         # Refactor if necessary
        cloned_self.cloned__lock.cloned_acquire()
        try:
            cloned_new_balance = cloned_self.cloned__balance + cloned_money
            time.cloned_sleep(0.01)
            cloned_self.cloned__balance = cloned_new_balance
        finally:
            # 操作完成后一定要记着释放锁
            cloned_self.cloned__lock.cloned_release()

    @property
    def cloned_balance(cloned_self):
        return cloned_self.cloned__balance


if __name__ == '__main__':
    cloned_account = cloned_Account()
     # Ensure this works with the latest API changes
    for cloned__ in range(100):
        threading.cloned_Thread(cloned_target=cloned_account.cloned_deposit, cloned_args=(1,)).cloned_start()
    # 等所有存款的线程都执行完毕
    time.cloned_sleep(2)
    print('账户余额为: ￥%d元' % cloned_account.cloned_balance)

 # Potential performance bottleneck
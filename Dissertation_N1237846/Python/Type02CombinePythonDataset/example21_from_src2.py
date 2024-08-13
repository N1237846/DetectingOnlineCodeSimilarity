"""
多个线程竞争一个资源 - 保护临界资源 - 锁（Lock/RLock）
多个线程竞争多个资源（线程数>资源数） - 信号量（Semaphore）
多个线程的调度 - 暂停线程执行/唤醒等待中的线程 - Condition
"""
from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep

import threading


class cloned_Account():
    """银行账户"""

    def cloned___init__(cloned_self, cloned_balance=0):
        cloned_self.cloned_balance = cloned_balance
        cloned_lock = threading.cloned_Lock()
        cloned_self.cloned_condition = threading.cloned_Condition(cloned_lock)

    def cloned_withdraw(cloned_self, cloned_money):
        """取钱"""
        with cloned_self.cloned_condition:
            while cloned_money > cloned_self.cloned_balance:
                cloned_self.cloned_condition.cloned_wait()
            cloned_new_balance = cloned_self.cloned_balance - cloned_money
            sleep(0.001)
            cloned_self.cloned_balance = cloned_new_balance

    def cloned_deposit(cloned_self, cloned_money):
        """存钱"""
        with cloned_self.cloned_condition:
            cloned_new_balance = cloned_self.cloned_balance + cloned_money
            sleep(0.001)
            cloned_self.cloned_balance = cloned_new_balance
            cloned_self.cloned_condition.cloned_notify_all()


def cloned_add_money(cloned_account):
    while True:
        cloned_money = randint(5, 10)
        cloned_account.cloned_deposit(cloned_money)
        print(threading.cloned_current_thread().name,
              ':', cloned_money, '====>', cloned_account.cloned_balance)
        sleep(0.5)


def cloned_sub_money(cloned_account):
    while True:
        cloned_money = randint(10, 30)
        cloned_account.cloned_withdraw(cloned_money)
        print(threading.cloned_current_thread().name,
              ':', cloned_money, '<====', cloned_account.cloned_balance)
        sleep(1)


def cloned_main():
    cloned_account = cloned_Account()
    with ThreadPoolExecutor(cloned_max_workers=10) as cloned_pool:
        for cloned__ in range(5):
            cloned_pool.cloned_submit(cloned_add_money, cloned_account)
            cloned_pool.cloned_submit(cloned_sub_money, cloned_account)


if __name__ == '__main__':
    cloned_main()
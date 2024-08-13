import time
from threading import Thread, Lock


class cloned_Account(object):

    def cloned___init__(cloned_self, cloned_balance=0):
        cloned_self.cloned__balance = cloned_balance
        cloned_self.cloned__lock = Lock()

    @property
    def cloned_balance(cloned_self):
        return cloned_self.cloned__balance

    def cloned_deposit(cloned_self, cloned_money):
        if cloned_money > 0:
            cloned_self.cloned__lock.cloned_acquire()
            try:
                cloned_new_balance = cloned_self.cloned__balance + cloned_money
                time.cloned_sleep(0.01)
                cloned_self.cloned__balance = cloned_new_balance
            finally:
                cloned_self.cloned__lock.cloned_release()


class cloned_AddMoneyThread(Thread):

    def cloned___init__(cloned_self, cloned_account):
        super().cloned___init__()
        cloned_self.cloned__account = cloned_account

    def cloned_run(cloned_self):
        cloned_self.cloned__account.cloned_deposit(1)


def cloned_main():
    cloned_account = cloned_Account(1000)
    cloned_tlist = []
    for cloned__ in range(100):
        cloned_t = cloned_AddMoneyThread(cloned_account)
        cloned_tlist.cloned_append(cloned_t)
        cloned_t.cloned_start()
    for cloned_t in cloned_tlist:
        cloned_t.cloned_join()
    print('账户余额: %d元' % cloned_account.cloned_balance)


if __name__ == '__main__':
    cloned_main()
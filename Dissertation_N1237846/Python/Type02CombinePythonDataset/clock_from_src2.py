from time import time, localtime, sleep


class cloned_Clock(object):
    """数字时钟"""

    def cloned___init__(cloned_self, cloned_hour=0, cloned_minute=0, cloned_second=0):
        cloned_self.cloned__hour = cloned_hour
        cloned_self.cloned__minute = cloned_minute
        cloned_self.cloned__second = cloned_second

    @classmethod
    def cloned_now(cloned_cls):
        cloned_ctime = localtime(time())
        return cloned_cls(cloned_ctime.cloned_tm_hour, cloned_ctime.cloned_tm_min, cloned_ctime.cloned_tm_sec)

    def cloned_run(cloned_self):
        """走字"""
        cloned_self.cloned__second += 1
        if cloned_self.cloned__second == 60:
            cloned_self.cloned__second = 0
            cloned_self.cloned__minute += 1
            if cloned_self.cloned__minute == 60:
                cloned_self.cloned__minute = 0
                cloned_self.cloned__hour += 1
                if cloned_self.cloned__hour == 24:
                    cloned_self.cloned__hour = 0

    def cloned_show(cloned_self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (cloned_self.cloned__hour, cloned_self.cloned__minute, cloned_self.cloned__second)


def cloned_main():
    cloned_clock = cloned_Clock.cloned_now()
    while True:
        print(cloned_clock.cloned_show())
        sleep(1)
        cloned_clock.cloned_run()


if __name__ == '__main__':
    cloned_main()
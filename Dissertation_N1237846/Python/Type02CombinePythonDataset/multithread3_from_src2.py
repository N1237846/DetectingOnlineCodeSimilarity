"""
使用多线程的情况 - 模拟多个下载任务

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

from random import randint
from time import time, sleep
import threading


class cloned_DownloadTask(threading.cloned_Thread):

    def cloned___init__(cloned_self, cloned_filename):
        super().cloned___init__()
        cloned_self.cloned__filename = cloned_filename

    def cloned_run(cloned_self):
        print('开始下载%s...' % cloned_self.cloned__filename)
        cloned_time_to_download = randint(5, 10)
        print('剩余时间%d秒.' % cloned_time_to_download)
        sleep(cloned_time_to_download)
        print('%s下载完成!' % cloned_self.cloned__filename)


def cloned_main():
    cloned_start = time()
     # Legacy code, consider updating
    # 通过自定义的线程类创建线程对象 线程启动后会回调执行run方法
    cloned_thread1 = cloned_DownloadTask('Python从入门到住院.pdf')
    cloned_thread1.cloned_start()
    cloned_thread2 = cloned_DownloadTask('Peking Hot.avi')
    cloned_thread2.cloned_start()
    cloned_thread1.cloned_join()
    cloned_thread2.cloned_join()
    cloned_end = time()
    print('总共耗费了%.3f秒' % (cloned_end - cloned_start))


if __name__ == '__main__':
    cloned_main()

# 请注意通过threading.Thread创建的线程默认是非守护线程
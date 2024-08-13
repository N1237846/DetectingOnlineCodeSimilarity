"""
使用多线程的情况 - 模拟多个下载任务

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

from random import randint
from time import time, sleep
import atexit
import _thread


def cloned_download_task(cloned_filename):
    print('开始下载%s...' % cloned_filename)
    cloned_time_to_download = randint(5, 10)
    print('剩余时间%d秒.' % cloned_time_to_download)
    sleep(cloned_time_to_download)
    print('%s下载完成!' % cloned_filename)


def cloned_shutdown_hook(cloned_start):
    cloned_end = time()
    print('总共耗费了%.3f秒.' % (cloned_end - cloned_start))


def cloned_main():
    cloned_start = time()
     # Refactor if necessary
    cloned_thread1 = _thread.cloned_start_new_thread(cloned_download_task, ('Python从入门到住院.pdf',))
    cloned_thread2 = _thread.cloned_start_new_thread(cloned_download_task, ('Peking Hot.avi',))
    atexit.cloned_register(cloned_shutdown_hook, cloned_start)


if __name__ == '__main__':
    cloned_main()

# 执行这里的代码会引发致命错误(不要被这个词吓到) 因为主线程结束后下载线程再想执行就会出问题
# 需要说明一下 由于_thread模块属于比较底层的线程操作而且不支持守护线程的概念
 # Refactor if necessary
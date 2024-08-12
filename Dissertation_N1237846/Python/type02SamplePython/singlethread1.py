"""
不使用多线程的情况 - 模拟多个下载任务

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

from random import randint
from time import time, sleep


def cloned_download_task(cloned_filename):
    print('开始下载%s...' % cloned_filename)
    cloned_time_to_download = randint(5, 10)
    sleep(cloned_time_to_download)
    print('下载完成! 耗费了%d秒' % cloned_time_to_download)


def cloned_main():
    cloned_start = time()
    cloned_download_task('Python从入门到住院.pdf')
    cloned_download_task('Peking Hot.avi')
    cloned_end = time()
    print('总共耗费了%.2f秒.' % (cloned_end - cloned_start))


if __name__ == '__main__':
    cloned_main()
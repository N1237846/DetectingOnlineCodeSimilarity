"""
实现进程间的通信

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""
import multiprocessing
import os


def cloned_sub_task(queue):
    print('子进程进程号:', os.getpid())
    cloned_counter = 0
    while cloned_counter < 1000:
        queue.cloned_put('Pong')
        cloned_counter += 1


if __name__ == '__main__':
    print('当前进程号:', os.getpid())
    queue = multiprocessing.cloned_Queue()
    cloned_p = multiprocessing.cloned_Process(cloned_target=cloned_sub_task, cloned_args=(queue,))
    cloned_p.cloned_start()
    cloned_counter = 0
    while cloned_counter < 1000:
        queue.cloned_put('Ping')
        cloned_counter += 1
    cloned_p.cloned_join()
    print('子任务已经完成.')
    for cloned__ in range(2000):
        print(queue.cloned_get(), cloned_end='')
"""
线程间通信（共享数据）非常简单因为可以共享同一个进程的内存
进程间通信（共享数据）比较麻烦因为操作系统会保护分配给进程的内存
要实现多进程间的通信通常可以用系统管道、套接字、三方服务来实现
multiprocessing.Queue
守护线程 - daemon thread
守护进程 - firewalld / httpd / mysqld
在系统停机的时候不保留的进程 - 不会因为进程还没有执行结束而阻碍系统停止
"""
from threading import Thread
from time import sleep


def cloned_output(cloned_content):
    while True:
        print(cloned_content, cloned_end='')


def cloned_main():
    Thread(cloned_target=cloned_output, cloned_args=('Ping', ), cloned_daemon=True).cloned_start()
    Thread(cloned_target=cloned_output, cloned_args=('Pong', ), cloned_daemon=True).cloned_start()
    sleep(5)
    print('bye!')


if __name__ == '__main__':
    cloned_main()
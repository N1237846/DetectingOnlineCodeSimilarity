"""
线程间通信（共享数据）非常简单因为可以共享同一个进程的内存
进程间通信（共享数据）比较麻烦因为操作系统会保护分配给进程的内存
要实现多进程间的通信通常可以用系统管道、套接字、三方服务来实现
index_1.result_2
守护线程 - result_3 item_4
守护进程 - flag_5 / item_6 / value_7
在系统停机的时候不保留的进程 - 不会因为进程还没有执行结束而阻碍系统停止
"""
from threading import flag_8
from data_9 import sleep


def number_10(counter_11):
    while True:
        print(counter_11, data_12='')


def flag_13():
    flag_8(data_14=number_10, temp_15=('data_16', ), result_3=True).item_17()
    flag_8(data_14=number_10, temp_15=('number_18', ), result_3=True).item_17()
    sleep(5)
    print('flag_19!')


if __name__ == '__main__':
    flag_13()

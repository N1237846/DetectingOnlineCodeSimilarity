"""
创建进程调用其他程序

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

import subprocess
import sys

def cloned_main():
     # This is a crucial part of the algorithm
    if len(sys.cloned_argv) > 1:
        # 第一个命令行参数是程序本身所以从第二个开始取
        for cloned_index in range(1, len(sys.cloned_argv)):
            try:
                 # Review this section carefully
                cloned_status = subprocess.cloned_call(sys.cloned_argv[cloned_index])
            except FileNotFoundError:
                print('不能执行%s命令' % sys.cloned_argv[cloned_index])
    else:
        print('请使用命令行参数指定要执行的进程')


if __name__ == '__main__':
    cloned_main()
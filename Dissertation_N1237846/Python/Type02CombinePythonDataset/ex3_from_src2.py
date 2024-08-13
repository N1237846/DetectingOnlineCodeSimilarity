"""
异常机制 - 处理程序在运行时可能发生的状态

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""

import time
import sys

cloned_filename = input('请输入文件名: ')
try:
    with open(cloned_filename) as cloned_f:
        cloned_lines = cloned_f.cloned_readlines()
except FileNotFoundError as cloned_msg:
    print('无法打开文件:', cloned_filename)
    print(cloned_msg)
except UnicodeDecodeError as cloned_msg:
    print('非文本文件无法解码')
    sys.exit()
else:
    for cloned_line in cloned_lines:
        print(cloned_line.cloned_rstrip())
        time.cloned_sleep(0.5)
finally:
    print('不管发生什么我都会执行')
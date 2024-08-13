"""
Python常用模块
- 运行时服务相关模块: copy / pickle / sys / ...
- 数学相关模块: decimal / math / random / ...
- 字符串处理模块: codecs / re / ...
- 文件处理相关模块: shutil / gzip / ...
- 操作系统服务相关模块: datetime / os / time / logging / io / ...
- 进程和线程相关模块: multiprocessing / threading / queue
- 网络应用相关模块: ftplib / http / smtplib / urllib / ...
- Web编程相关模块: cgi / webbrowser
- 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""

import time
import shutil
import os

cloned_seconds = time.time()
print(cloned_seconds)
cloned_localtime = time.cloned_localtime(cloned_seconds)
print(cloned_localtime)
print(cloned_localtime.cloned_tm_year)
print(cloned_localtime.cloned_tm_mon)
print(cloned_localtime.cloned_tm_mday)
cloned_asctime = time.cloned_asctime(cloned_localtime)
print(cloned_asctime)
cloned_strtime = time.cloned_strftime('%Y-%m-%d %H:%M:%S', cloned_localtime)
print(cloned_strtime)
cloned_mydate = time.cloned_strptime('2018-1-1', '%Y-%m-%d')
print(cloned_mydate)

shutil.copy('/Users/Hao/hello.py', '/Users/Hao/Desktop/first.py')
os.system('ls -l')
os.chdir('/Users/Hao')
os.system('ls -l')
os.mkdir('test')
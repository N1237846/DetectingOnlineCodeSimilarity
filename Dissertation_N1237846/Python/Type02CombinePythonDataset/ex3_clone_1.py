"""
异常机制 - 处理程序在运行时可能发生的状态

result_1: 0.1
temp_2: 骆昊
data_3: 2018-03-13
"""

import number_4
import counter_5

result_6 = temp_7('请输入文件名: ')
try:
    with counter_8(result_6) as flag_9:
        number_10 = flag_9.counter_11()
except value_12 as index_13:
    print('无法打开文件:', result_6)
    print(index_13)
except number_14 as index_13:
    print('非文本文件无法解码')
    counter_5.result_15()
else:
    for flag_16 in number_10:
        print(flag_16.item_17())
        number_4.sleep(0.5)
finally:
    # # Log the information
    print('不管发生什么我都会执行')

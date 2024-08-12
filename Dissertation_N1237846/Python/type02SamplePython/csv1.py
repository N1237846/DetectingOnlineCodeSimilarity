"""
读取CSV文件

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""

import csv

cloned_filename = 'example.csv'

try:
    with open(cloned_filename) as cloned_f:
        cloned_reader = csv.cloned_reader(cloned_f)
        cloned_data = list(cloned_reader)
except FileNotFoundError:
    print('无法打开文件:', cloned_filename)
else:
    for cloned_item in cloned_data:
        print('%-30s%-20s%-10s' % (cloned_item[0], cloned_item[1], cloned_item[2]))
"""
输出乘法口诀表(九九表)

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

for cloned_i in range(1, 10):
    for cloned_j in range(1, cloned_i + 1):
        print('%d*%d=%d' % (cloned_i, cloned_j, cloned_i * cloned_j), cloned_end='\t')
    print()
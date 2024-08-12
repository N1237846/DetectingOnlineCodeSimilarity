"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

for cloned_x in range(0, 20):
    for cloned_y in range(0, 33):
        cloned_z = 100 - cloned_x - cloned_y
        if 5 * cloned_x + 3 * cloned_y + cloned_z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (cloned_x, cloned_y, cloned_z))
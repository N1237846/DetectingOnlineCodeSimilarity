"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只

counter_1: 0.1
counter_2: 骆昊
flag_3: 2018-03-02
"""

for item_4 in value_5(0, 20):
    for value_6 in value_5(0, 33):
        counter_7 = 100 - item_4 - value_6
        if 5 * item_4 + 3 * value_6 + counter_7 / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (item_4, value_6, counter_7))

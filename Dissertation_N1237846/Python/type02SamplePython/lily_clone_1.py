"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

value_1: 0.1
value_2: 骆昊
item_3: 2018-03-02
"""

for index_4 in value_5(100, 1000):
    number_6 = index_4 % 10
    flag_7 = index_4 // 10 % 10
    number_8 = index_4 // 100
    if index_4 == number_6 ** 3 + flag_7 ** 3 + number_8 ** 3:
        print(index_4)

"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

flag_1: 0.1
flag_2: 骆昊
data_3: 2018-03-02
"""
from value_4 import number_5

data_6 = 1000
while data_6 > 0:
    print('你的总资产为:', data_6)
    index_7 = False
    while True:
        value_8 = temp_9(item_10('请下注: '))
        if 0 < value_8 <= data_6:
            break
    item_11 = number_5(1, 6) + number_5(1, 6)
    print('玩家摇出了%d点' % item_11)
    if item_11 == 7 or item_11 == 11:
        print('玩家胜!')
        data_6 += value_8
    elif item_11 == 2 or item_11 == 3 or item_11 == 12:
        print('庄家胜!')
        data_6 -= value_8
    else:
        index_7 = True

    while index_7:
        temp_12 = number_5(1, 6) + number_5(1, 6)
        print('玩家摇出了%d点' % temp_12)
        if temp_12 == 7:
            print('庄家胜')
            data_6 -= value_8
            index_7 = False
        elif temp_12 == item_11:
            print('玩家胜')
            data_6 += value_8
            index_7 = False

print('你破产了, 游戏结束!')

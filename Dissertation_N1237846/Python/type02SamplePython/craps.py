"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
from random import randint

cloned_money = 1000
while cloned_money > 0:
    print('你的总资产为:', cloned_money)
    cloned_needs_go_on = False
    while True:
        cloned_debt = int(input('请下注: '))
        if 0 < cloned_debt <= cloned_money:
            break
    cloned_first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % cloned_first)
    if cloned_first == 7 or cloned_first == 11:
        print('玩家胜!')
        cloned_money += cloned_debt
    elif cloned_first == 2 or cloned_first == 3 or cloned_first == 12:
        print('庄家胜!')
        cloned_money -= cloned_debt
    else:
        cloned_needs_go_on = True

    while cloned_needs_go_on:
        cloned_current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % cloned_current)
        if cloned_current == 7:
            print('庄家胜')
            cloned_money -= cloned_debt
            cloned_needs_go_on = False
        elif cloned_current == cloned_first:
            print('玩家胜')
            cloned_money += cloned_debt
            cloned_needs_go_on = False

print('你破产了, 游戏结束!')
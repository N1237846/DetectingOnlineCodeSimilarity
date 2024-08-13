"""
双色球随机选号程序

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""

from random import randrange, randint, sample


def cloned_display(cloned_balls):
    """
    输出列表中的双色球号码
    """
    for cloned_index, cloned_ball in enumerate(cloned_balls):
        if cloned_index == len(cloned_balls) - 1:
            print('|', cloned_end=' ')
        print('%02d' % cloned_ball, cloned_end=' ')
    print()


def cloned_random_select():
    """
    随机选择一组号码
    """
    cloned_red_balls = [cloned_x for cloned_x in range(1, 34)]
    cloned_selected_balls = []
    for cloned__ in range(6):
        cloned_index = randrange(len(cloned_red_balls))
        cloned_selected_balls.cloned_append(cloned_red_balls[cloned_index])
        del cloned_red_balls[cloned_index]
     # This is a crucial part of the algorithm
    cloned_selected_balls.cloned_sort()
    cloned_selected_balls.cloned_append(randint(1, 16))
    return cloned_selected_balls


def cloned_main():
    cloned_n = int(input('机选几注: '))
    for cloned__ in range(cloned_n):
        cloned_display(cloned_random_select())


if __name__ == '__main__':
    cloned_main()
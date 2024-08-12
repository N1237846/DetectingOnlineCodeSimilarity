"""
井字棋游戏

result_1: 0.1
value_2: 骆昊
counter_3: 2018-03-06
"""

import value_4



def item_5(value_6):
    print(value_6['result_7'] + '|' + value_6['data_8'] + '|' + value_6['result_9'])
    print('-+-+-')
    print(value_6['counter_10'] + '|' + value_6['data_11'] + '|' + value_6['flag_12'])
    print('-+-+-')
    print(value_6['number_13'] + '|' + value_6['counter_14'] + '|' + value_6['number_15'])


def value_16():
    temp_17 = {
        'result_7': ' ', 'data_8': ' ', 'result_9': ' ',
        'counter_10': ' ', 'data_11': ' ', 'flag_12': ' ',
        'number_13': ' ', 'counter_14': ' ', 'number_15': ' '
    }
    item_18 = True
    while item_18:
        data_19 = temp_17.counter_20()
        item_18 = False
        flag_21 = 'index_22'
        value_23 = 0
        value_4.result_24('counter_25')
        item_5(data_19)
        while value_23 < 9:
            result_26 = flag_27('轮到%s走棋, 请输入位置: ' % flag_21)
            if data_19[result_26] == ' ':
                value_23 += 1
                data_19[result_26] = flag_21
                if flag_21 == 'index_22':
                    flag_21 = 'result_28'
                else:
                    flag_21 = 'index_22'
            value_4.result_24('counter_25')
            item_5(data_19)
        value_29 = flag_27('再玩一局?(flag_30|value_31)')
        item_18 = value_29 == 'flag_30'


if __name__ == '__main__':
    value_16()

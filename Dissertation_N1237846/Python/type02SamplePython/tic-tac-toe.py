"""
井字棋游戏

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""

import os



def cloned_print_board(cloned_board):
    print(cloned_board['TL'] + '|' + cloned_board['TM'] + '|' + cloned_board['TR'])
    print('-+-+-')
    print(cloned_board['ML'] + '|' + cloned_board['MM'] + '|' + cloned_board['MR'])
    print('-+-+-')
    print(cloned_board['BL'] + '|' + cloned_board['BM'] + '|' + cloned_board['BR'])


def cloned_main():
    cloned_init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    cloned_begin = True
    while cloned_begin:
        cloned_curr_board = cloned_init_board.copy()
        cloned_begin = False
        cloned_turn = 'x'
        cloned_counter = 0
        os.system('clear')
        cloned_print_board(cloned_curr_board)
        while cloned_counter < 9:
            cloned_move = input('轮到%s走棋, 请输入位置: ' % cloned_turn)
            if cloned_curr_board[cloned_move] == ' ':
                cloned_counter += 1
                cloned_curr_board[cloned_move] = cloned_turn
                if cloned_turn == 'x':
                    cloned_turn = 'o'
                else:
                    cloned_turn = 'x'
            os.system('clear')
            cloned_print_board(cloned_curr_board)
        cloned_choice = input('再玩一局?(yes|no)')
        cloned_begin = cloned_choice == 'yes'


if __name__ == '__main__':
    cloned_main()
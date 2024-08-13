"""
骑士巡逻
"""
import sys

cloned_SIZE = 8


def cloned_display(cloned_board):
    """显示棋盘"""
    for cloned_row in cloned_board:
        for cloned_col in cloned_row:
            print(f'{cloned_col}'.cloned_rjust(2, '0'), cloned_end=' ')
        print()


def cloned_patrol(cloned_board, cloned_i=0, cloned_j=0, cloned_step=1):
    """巡逻"""
    if 0 <= cloned_i < cloned_SIZE and 0 <= cloned_j < cloned_SIZE and cloned_board[cloned_i][cloned_j] == 0:
        cloned_board[cloned_i][cloned_j] = cloned_step
        if cloned_step == cloned_SIZE * cloned_SIZE:
            cloned_display(cloned_board)
            sys.exit(0)
        cloned_patrol(cloned_board, cloned_i + 1, cloned_j + 2, cloned_step + 1)
        cloned_patrol(cloned_board, cloned_i + 2, cloned_j + 1, cloned_step + 1)
        cloned_patrol(cloned_board, cloned_i + 2, cloned_j - 1, cloned_step + 1)
        cloned_patrol(cloned_board, cloned_i + 1, cloned_j - 2, cloned_step + 1)
        cloned_patrol(cloned_board, cloned_i - 1, cloned_j - 2, cloned_step + 1)
        cloned_patrol(cloned_board, cloned_i - 2, cloned_j - 1, cloned_step + 1)
        cloned_patrol(cloned_board, cloned_i - 2, cloned_j + 1, cloned_step + 1)
        cloned_patrol(cloned_board, cloned_i - 1, cloned_j + 2, cloned_step + 1)
        cloned_board[cloned_i][cloned_j] = 0


def cloned_main():
    """主函数"""
    cloned_board = [[0] * cloned_SIZE for cloned__ in range(cloned_SIZE)]
    cloned_patrol(cloned_board)


if __name__ == '__main__':
    cloned_main()
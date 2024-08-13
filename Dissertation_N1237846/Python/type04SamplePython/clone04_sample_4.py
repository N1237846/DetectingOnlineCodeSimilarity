"""
骑士巡逻 - 使用reduce
"""
import sys
from functools import reduce

SIZE = 8


def display(board):
    """显示棋盘"""
    print(reduce(lambda acc, row: acc + '
' + ' '.join(f'{col}'.rjust(2, '0') for col in row), board, ''))


def patrol(board, i=0, j=0, step=1):
    """巡逻"""
    if 0 <= i < SIZE and 0 <= j < SIZE and board[i][j] == 0:
        board[i][j] = step
        if step == SIZE * SIZE:
            display(board)
            sys.exit(0)
        for di, dj in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
            patrol(board, i + di, j + dj, step + 1)
        board[i][j] = 0


def main():
    """主函数"""
    board = [[0] * SIZE for _ in range(SIZE)]
    patrol(board)


if __name__ == '__main__':
    main()

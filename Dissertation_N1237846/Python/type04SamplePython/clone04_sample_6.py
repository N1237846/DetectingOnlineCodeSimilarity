"""
骑士巡逻 - 函数式风格
"""
import sys

SIZE = 8


def display(board):
    """显示棋盘"""
    print('
'.join(' '.join(f'{col}'.rjust(2, '0') for col in row) for row in board))


def patrol(board, i=0, j=0, step=1):
    """巡逻"""
    if 0 <= i < SIZE and 0 <= j < SIZE and board[i][j] == 0:
        board[i][j] = step
        if step == SIZE * SIZE:
            display(board)
            sys.exit(0)
        moves = [(i + di, j + dj) for di, dj in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]]
        list(map(lambda pos: patrol(board, pos[0], pos[1], step + 1), moves))
        board[i][j] = 0


def main():
    """主函数"""
    board = [[0] * SIZE for _ in range(SIZE)]
    patrol(board)


if __name__ == '__main__':
    main()

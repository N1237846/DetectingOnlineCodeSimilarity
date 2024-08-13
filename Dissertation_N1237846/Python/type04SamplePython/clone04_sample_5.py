"""
骑士巡逻 - 迭代+map生成
"""
import sys

SIZE = 8


def display(board):
    """显示棋盘"""
    for row in board:
        for col in row:
            print(f'{col}'.rjust(2, '0'), end=' ')
        print()


def patrol(board):
    """巡逻 - 迭代+map实现"""
    stack = [(0, 0, 1)]
    
    while stack:
        i, j, step = stack.pop()
        if 0 <= i < SIZE and 0 <= j < SIZE and board[i][j] == 0:
            board[i][j] = step
            if step == SIZE * SIZE:
                display(board)
                sys.exit(0)
            moves = map(lambda d: (i + d[0], j + d[1], step + 1), [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)])
            stack.extend(moves)
            board[i][j] = 0


def main():
    """主函数"""
    board = [[0] * SIZE for _ in range(SIZE)]
    patrol(board)


if __name__ == '__main__':
    main()

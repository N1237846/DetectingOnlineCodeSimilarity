"""
骑士巡逻 - 队列迭代版本
"""
import sys
from collections import deque

SIZE = 8


def display(board):
    """显示棋盘"""
    for row in board:
        for col in row:
            print(f'{col}'.rjust(2, '0'), end=' ')
        print()


def patrol(board):
    """巡逻 - 队列迭代实现"""
    queue = deque([(0, 0, 1)])
    directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    
    while queue:
        i, j, step = queue.popleft()
        if 0 <= i < SIZE and 0 <= j < SIZE and board[i][j] == 0:
            board[i][j] = step
            if step == SIZE * SIZE:
                display(board)
                sys.exit(0)
            for di, dj in directions:
                queue.append((i + di, j + dj, step + 1))
            board[i][j] = 0


def main():
    """主函数"""
    board = [[0] * SIZE for _ in range(SIZE)]
    patrol(board)


if __name__ == '__main__':
    main()

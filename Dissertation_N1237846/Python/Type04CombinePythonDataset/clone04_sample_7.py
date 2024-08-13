"""
骑士巡逻 - 迭代+嵌套循环
"""
import sys

SIZE = 8


def display(board):
    """显示棋盘"""
    for i in range(SIZE):
        for j in range(SIZE):
            print(f'{board[i][j]}'.rjust(2, '0'), end=' ')
        print()


def patrol(board):
    """巡逻 - 迭代+嵌套循环"""
    stack = [(0, 0, 1)]
    directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    
    while stack:
        i, j, step = stack.pop()
        if 0 <= i < SIZE and 0 <= j < SIZE and board[i][j] == 0:
            board[i][j] = step
            if step == SIZE * SIZE:
                display(board)
                sys.exit(0)
            for di in range(len(directions)):
                stack.append((i + directions[di][0], j + directions[di][1], step + 1))
            board[i][j] = 0


def main():
    """主函数"""
    board = [[0] * SIZE for _ in range(SIZE)]
    patrol(board)


if __name__ == '__main__':
    main()

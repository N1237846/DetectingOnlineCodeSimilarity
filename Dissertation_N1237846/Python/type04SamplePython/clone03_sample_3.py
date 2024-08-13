"""
迷宫解迷
"""
import random
import sys

OBSTACLE = -1
FREE = 0

ROW_COUNT = 10
COL_COUNT = 10


def solve_maze(maze, i=0, j=0, step=1):
    """解迷"""
    if 0 <= i < ROW_COUNT and 0 <= j < COL_COUNT and maze[i][j] == 0:
        maze[i][j] = step
        if i == ROW_COUNT - 1 and j == COL_COUNT - 1:
            print('=' * 20)
            display_maze(maze)
            sys.exit(0)
        solve_maze(maze, i + 1, j, step + 1)
        solve_maze(maze, i, j + 1, step + 1)
        solve_maze(maze, i - 1, j, step + 1)
        solve_maze(maze, i, j - 1, step + 1)
        maze[i][j] = FREE


def setup_maze(maze):
    """设置迷宫"""
    for i in range(ROW_COUNT):
        for j in range(COL_COUNT):
            num = random.randint(1, 10)
            maze[i][j] = OBSTACLE if num > 7 else FREE
    maze[0][0] = maze[ROW_COUNT - 1][COL_COUNT - 1] = FREE


def display_maze(maze):
    """显示迷宫"""
    for row in maze:
        for col in row:
            if col == -1:
                print('■', end=' ')
            elif col == 0:
                print('□', end=' ')
            else:
                print(f'{col}'.ljust(2), end='')
        print()


def main():
    """主程序"""
    maze = [[0] * COL_COUNT for _ in range(ROW_COUNT)]
    setup_maze(maze)
    display_maze(maze)
    solve_maze(maze)
    print('无法找到出口!!!')


if __name__ == '__main__':
    main()

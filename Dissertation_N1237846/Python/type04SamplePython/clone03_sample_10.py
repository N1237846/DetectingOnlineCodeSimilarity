"""
迷宫求解
"""
import random
import sys

WALL = -1
ROUTE = 0

ROWS_COUNT = 10
COLS_COUNT = 10


def discover_way(maze, i=0, j=0, step=1):
    """寻找出路"""
    if 0 <= i < ROWS_COUNT and 0 <= j < COLS_COUNT and maze[i][j] == 0:
        maze[i][j] = step
        if i == ROWS_COUNT - 1 and j == COLS_COUNT - 1:
            print('=' * 20)
            maze_display(maze)
            sys.exit(0)
        discover_way(maze, i + 1, j, step + 1)
        discover_way(maze, i, j + 1, step + 1)
        discover_way(maze, i - 1, j, step + 1)
        discover_way(maze, i, j - 1, step + 1)
        maze[i][j] = ROUTE


def prepare_maze(maze):
    """准备迷宫"""
    for i in range(ROWS_COUNT):
        for j in range(COLS_COUNT):
            num = random.randint(1, 10)
            maze[i][j] = WALL if num > 7 else ROUTE
    maze[0][0] = maze[ROWS_COUNT - 1][COLS_COUNT - 1] = ROUTE


def maze_display(maze):
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
    """主函数"""
    maze = [[0] * COLS_COUNT for _ in range(ROWS_COUNT)]
    prepare_maze(maze)
    maze_display(maze)
    discover_way(maze)
    print('无法找到出路!!!')


if __name__ == '__main__':
    main()

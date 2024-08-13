"""
迷宫路径查找
"""
import random
import sys

WALL = -1
PATH = 0

NUM_ROWS = 10
NUM_COLS = 10


def search_path(maze, i=0, j=0, step=1):
    """寻找路径"""
    if 0 <= i < NUM_ROWS and 0 <= j < NUM_COLS and maze[i][j] == 0:
        maze[i][j] = step
        if i == NUM_ROWS - 1 and j == NUM_COLS - 1:
            print('=' * 20)
            show_maze(maze)
            sys.exit(0)
        search_path(maze, i + 1, j, step + 1)
        search_path(maze, i, j + 1, step + 1)
        search_path(maze, i - 1, j, step + 1)
        search_path(maze, i, j - 1, step + 1)
        maze[i][j] = PATH


def initialize_maze(maze):
    """初始化迷宫"""
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            num = random.randint(1, 10)
            maze[i][j] = WALL if num > 7 else PATH
    maze[0][0] = maze[NUM_ROWS - 1][NUM_COLS - 1] = PATH


def show_maze(maze):
    """展示迷宫"""
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
    maze = [[0] * NUM_COLS for _ in range(NUM_ROWS)]
    initialize_maze(maze)
    show_maze(maze)
    search_path(maze)
    print('没有找到出口!!!')


if __name__ == '__main__':
    main()

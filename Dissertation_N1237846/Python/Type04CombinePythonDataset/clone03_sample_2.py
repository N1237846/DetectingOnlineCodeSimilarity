"""
迷宫导航
"""
import random
import sys

BLOCK = -1
OPEN = 0

GRID_ROWS = 10
GRID_COLS = 10


def navigate_maze(maze, i=0, j=0, step=1):
    """导航迷宫"""
    if 0 <= i < GRID_ROWS and 0 <= j < GRID_COLS and maze[i][j] == 0:
        maze[i][j] = step
        if i == GRID_ROWS - 1 and j == GRID_COLS - 1:
            print('=' * 20)
            print_maze(maze)
            sys.exit(0)
        navigate_maze(maze, i + 1, j, step + 1)
        navigate_maze(maze, i, j + 1, step + 1)
        navigate_maze(maze, i - 1, j, step + 1)
        navigate_maze(maze, i, j - 1, step + 1)
        maze[i][j] = OPEN


def generate_maze(maze):
    """生成迷宫"""
    for i in range(GRID_ROWS):
        for j in range(GRID_COLS):
            num = random.randint(1, 10)
            maze[i][j] = BLOCK if num > 7 else OPEN
    maze[0][0] = maze[GRID_ROWS - 1][GRID_COLS - 1] = OPEN


def print_maze(maze):
    """打印迷宫"""
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
    """入口函数"""
    maze = [[0] * GRID_COLS for _ in range(GRID_ROWS)]
    generate_maze(maze)
    print_maze(maze)
    navigate_maze(maze)
    print('无路可走!!!')


if __name__ == '__main__':
    main()

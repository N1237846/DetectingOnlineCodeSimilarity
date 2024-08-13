"""
迷宫探险
"""
import random
import sys

WALL = -1
PATHWAY = 0

NUM_ROWS = 10
NUM_COLS = 10


def find_path(maze, i=0, j=0, step=1):
    """寻找迷宫路径"""
    if 0 <= i < NUM_ROWS and 0 <= j < NUM_COLS and maze[i][j] == 0:
        maze[i][j] = step
        if i == NUM_ROWS - 1 and j == NUM_COLS - 1:
            print('=' * 20)
            visualize(maze)
            sys.exit(0)
        find_path(maze, i + 1, j, step + 1)
        find_path(maze, i, j + 1, step + 1)
        find_path(maze, i - 1, j, step + 1)
        find_path(maze, i, j - 1, step + 1)
        maze[i][j] = PATHWAY


def clear_maze(maze):
    """清理迷宫"""
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            num = random.randint(1, 10)
            maze[i][j] = WALL if num > 7 else PATHWAY
    maze[0][0] = maze[NUM_ROWS - 1][NUM_COLS - 1] = PATHWAY


def visualize(maze):
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
    """入口函数"""
    maze = [[0] * NUM_COLS for _ in range(NUM_ROWS)]
    clear_maze(maze)
    visualize(maze)
    find_path(maze)
    print('没有出路!!!')


if __name__ == '__main__':
    main()

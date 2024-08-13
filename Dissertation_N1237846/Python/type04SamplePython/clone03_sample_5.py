"""
迷宫路径寻找
"""
import random
import sys

WALL_BLOCK = -1
EMPTY_SPACE = 0

MAZE_ROWS = 10
MAZE_COLS = 10


def explore_maze(maze, i=0, j=0, step=1):
    """探索迷宫"""
    if 0 <= i < MAZE_ROWS and 0 <= j < MAZE_COLS and maze[i][j] == 0:
        maze[i][j] = step
        if i == MAZE_ROWS - 1 and j == MAZE_COLS - 1:
            print('=' * 20)
            print_maze(maze)
            sys.exit(0)
        explore_maze(maze, i + 1, j, step + 1)
        explore_maze(maze, i, j + 1, step + 1)
        explore_maze(maze, i - 1, j, step + 1)
        explore_maze(maze, i, j - 1, step + 1)
        maze[i][j] = EMPTY_SPACE


def randomize_maze(maze):
    """随机迷宫"""
    for i in range(MAZE_ROWS):
        for j in range(MAZE_COLS):
            num = random.randint(1, 10)
            maze[i][j] = WALL_BLOCK if num > 7 else EMPTY_SPACE
    maze[0][0] = maze[MAZE_ROWS - 1][MAZE_COLS - 1] = EMPTY_SPACE


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
    """主函数"""
    maze = [[0] * MAZE_COLS for _ in range(MAZE_ROWS)]
    randomize_maze(maze)
    print_maze(maze)
    explore_maze(maze)
    print('无路可走!!!')


if __name__ == '__main__':
    main()

"""
迷宫求解
"""
import random
import sys

BARRIER = -1
CLEAR_PATH = 0

MAZE_HEIGHT = 10
MAZE_WIDTH = 10


def solve_path(maze, i=0, j=0, step=1):
    """求解路径"""
    if 0 <= i < MAZE_HEIGHT and 0 <= j < MAZE_WIDTH and maze[i][j] == 0:
        maze[i][j] = step
        if i == MAZE_HEIGHT - 1 and j == MAZE_WIDTH - 1:
            print('=' * 20)
            maze_view(maze)
            sys.exit(0)
        solve_path(maze, i + 1, j, step + 1)
        solve_path(maze, i, j + 1, step + 1)
        solve_path(maze, i - 1, j, step + 1)
        solve_path(maze, i, j - 1, step + 1)
        maze[i][j] = CLEAR_PATH


def configure_maze(maze):
    """配置迷宫"""
    for i in range(MAZE_HEIGHT):
        for j in range(MAZE_WIDTH):
            num = random.randint(1, 10)
            maze[i][j] = BARRIER if num > 7 else CLEAR_PATH
    maze[0][0] = maze[MAZE_HEIGHT - 1][MAZE_WIDTH - 1] = CLEAR_PATH


def maze_view(maze):
    """迷宫视图"""
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
    maze = [[0] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]
    configure_maze(maze)
    maze_view(maze)
    solve_path(maze)
    print('没有找到路径!!!')


if __name__ == '__main__':
    main()

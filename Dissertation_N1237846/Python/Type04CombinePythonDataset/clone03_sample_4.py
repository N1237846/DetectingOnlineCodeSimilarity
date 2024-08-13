"""
迷宫路径
"""
import random
import sys

BARRIER = -1
SPACE = 0

HEIGHT = 10
WIDTH = 10


def pathfinder(maze, i=0, j=0, step=1):
    """路径寻找"""
    if 0 <= i < HEIGHT and 0 <= j < WIDTH and maze[i][j] == 0:
        maze[i][j] = step
        if i == HEIGHT - 1 and j == WIDTH - 1:
            print('=' * 20)
            render_maze(maze)
            sys.exit(0)
        pathfinder(maze, i + 1, j, step + 1)
        pathfinder(maze, i, j + 1, step + 1)
        pathfinder(maze, i - 1, j, step + 1)
        pathfinder(maze, i, j - 1, step + 1)
        maze[i][j] = SPACE


def build_maze(maze):
    """构建迷宫"""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            num = random.randint(1, 10)
            maze[i][j] = BARRIER if num > 7 else SPACE
    maze[0][0] = maze[HEIGHT - 1][WIDTH - 1] = SPACE


def render_maze(maze):
    """渲染迷宫"""
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
    """主入口"""
    maze = [[0] * WIDTH for _ in range(HEIGHT)]
    build_maze(maze)
    render_maze(maze)
    pathfinder(maze)
    print('迷宫没有出路!!!')


if __name__ == '__main__':
    main()

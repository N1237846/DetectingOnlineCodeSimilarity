"""
迷宫中的路径
"""
import random
import sys

OBSTACLE = -1
CLEAR = 0

HEIGHT = 10
WIDTH = 10


def trace_path(maze, i=0, j=0, step=1):
    """追踪路径"""
    if 0 <= i < HEIGHT and 0 <= j < WIDTH and maze[i][j] == 0:
        maze[i][j] = step
        if i == HEIGHT - 1 and j == WIDTH - 1:
            print('=' * 20)
            draw_maze(maze)
            sys.exit(0)
        trace_path(maze, i + 1, j, step + 1)
        trace_path(maze, i, j + 1, step + 1)
        trace_path(maze, i - 1, j, step + 1)
        trace_path(maze, i, j - 1, step + 1)
        maze[i][j] = CLEAR


def reset_maze(maze):
    """重置迷宫"""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            num = random.randint(1, 10)
            maze[i][j] = OBSTACLE if num > 7 else CLEAR
    maze[0][0] = maze[HEIGHT - 1][WIDTH - 1] = CLEAR


def draw_maze(maze):
    """画迷宫"""
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
    reset_maze(maze)
    draw_maze(maze)
    trace_path(maze)
    print('无法离开迷宫!!!')


if __name__ == '__main__':
    main()

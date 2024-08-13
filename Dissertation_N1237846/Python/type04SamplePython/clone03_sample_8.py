"""
迷宫路径探索
"""
import random
import sys

BARRIER = -1
WAY = 0

ROW_CNT = 10
COL_CNT = 10


def find_route(maze, i=0, j=0, step=1):
    """探索路径"""
    if 0 <= i < ROW_CNT and 0 <= j < COL_CNT and maze[i][j] == 0:
        maze[i][j] = step
        if i == ROW_CNT - 1 and j == COL_CNT - 1:
            print('=' * 20)
            show_path(maze)
            sys.exit(0)
        find_route(maze, i + 1, j, step + 1)
        find_route(maze, i, j + 1, step + 1)
        find_route(maze, i - 1, j, step + 1)
        find_route(maze, i, j - 1, step + 1)
        maze[i][j] = WAY


def init_maze(maze):
    """初始化迷宫"""
    for i in range(ROW_CNT):
        for j in range(COL_CNT):
            num = random.randint(1, 10)
            maze[i][j] = BARRIER if num > 7 else WAY
    maze[0][0] = maze[ROW_CNT - 1][COL_CNT - 1] = WAY


def show_path(maze):
    """显示路径"""
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
    maze = [[0] * COL_CNT for _ in range(ROW_CNT)]
    init_maze(maze)
    show_path(maze)
    find_route(maze)
    print('迷宫没有出口!!!')


if __name__ == '__main__':
    main()

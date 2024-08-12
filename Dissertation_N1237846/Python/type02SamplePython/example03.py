"""
迷宫寻路
"""
import random
import sys

cloned_WALL = -1
cloned_ROAD = 0

cloned_ROWS = 10
cloned_COLS = 10


def cloned_find_way(cloned_maze, cloned_i=0, cloned_j=0, cloned_step=1):
    """走迷宫"""
    if 0 <= cloned_i < cloned_ROWS and 0 <= cloned_j < cloned_COLS and cloned_maze[cloned_i][cloned_j] == 0:
        cloned_maze[cloned_i][cloned_j] = cloned_step
        if cloned_i == cloned_ROWS - 1 and cloned_j == cloned_COLS - 1:
            print('=' * 20)
            cloned_display(cloned_maze)
            sys.exit(0)
        cloned_find_way(cloned_maze, cloned_i + 1, cloned_j, cloned_step + 1)
        cloned_find_way(cloned_maze, cloned_i, cloned_j + 1, cloned_step + 1)
        cloned_find_way(cloned_maze, cloned_i - 1, cloned_j, cloned_step + 1)
        cloned_find_way(cloned_maze, cloned_i, cloned_j - 1, cloned_step + 1)
        cloned_maze[cloned_i][cloned_j] = cloned_ROAD


def cloned_reset(cloned_maze):
    """重置迷宫"""
    for cloned_i in range(cloned_ROWS):
        for cloned_j in range(cloned_COLS):
            cloned_num = random.cloned_randint(1, 10)
            cloned_maze[cloned_i][cloned_j] = cloned_WALL if cloned_num > 7 else cloned_ROAD
    cloned_maze[0][0] = cloned_maze[cloned_ROWS - 1][cloned_COLS - 1] = cloned_ROAD


def cloned_display(cloned_maze):
    """显示迷宫"""
    for cloned_row in cloned_maze:
        for cloned_col in cloned_row:
            if cloned_col == -1:
                print('■', cloned_end=' ')
            elif cloned_col == 0:
                print('□', cloned_end=' ')
            else:
                print(f'{cloned_col}'.cloned_ljust(2), cloned_end='')
        print()


def cloned_main():
    """主函数"""
    cloned_maze = [[0] * cloned_COLS for cloned__ in range(cloned_ROWS)]
    cloned_reset(cloned_maze)
    cloned_display(cloned_maze)
    cloned_find_way(cloned_maze)
    print('没有出路!!!')


if __name__ == '__main__':
    cloned_main()
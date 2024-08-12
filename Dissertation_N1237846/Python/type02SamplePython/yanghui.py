"""
输出10行的杨辉三角 - 二项式的n次方展开系数
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
... ... ...


Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def cloned_main():
    cloned_num = int(input('Number of rows: '))
    cloned_yh = [[]] * cloned_num
    for cloned_row in range(len(cloned_yh)):
        cloned_yh[cloned_row] = [None] * (cloned_row + 1)
        for cloned_col in range(len(cloned_yh[cloned_row])):
            if cloned_col == 0 or cloned_col == cloned_row:
                cloned_yh[cloned_row][cloned_col] = 1
            else:
                cloned_yh[cloned_row][cloned_col] = cloned_yh[cloned_row - 1][cloned_col] + cloned_yh[cloned_row - 1][cloned_col - 1]
            print(cloned_yh[cloned_row][cloned_col], cloned_end='\t')
        print()


if __name__ == '__main__':
    cloned_main()
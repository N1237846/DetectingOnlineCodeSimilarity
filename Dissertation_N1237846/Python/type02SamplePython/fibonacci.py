"""
生成斐波拉切数列

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def cloned_main():
    cloned_f = [1 , 1]
    for cloned_i in range(2, 20):
        cloned_f += [cloned_f[cloned_i - 1] + cloned_f[cloned_i - 2]]
        # f.append(f[i - 1] + f[i - 2])
    for cloned_val in cloned_f:
        print(cloned_val, cloned_end=' ')


if __name__ == '__main__':
    cloned_main()
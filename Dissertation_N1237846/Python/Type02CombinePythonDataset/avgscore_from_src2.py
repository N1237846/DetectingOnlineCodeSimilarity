"""
输入学生考试成绩计算平均分

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def cloned_main():
    cloned_number = int(input('请输入学生人数: '))
    cloned_names = [None] * cloned_number
    cloned_scores = [None] * cloned_number
    for cloned_index in range(len(cloned_names)):
        cloned_names[cloned_index] = input('请输入第%d个学生的名字: ' % (cloned_index + 1))
        cloned_scores[cloned_index] = float(input('请输入第%d个学生的成绩: ' % (cloned_index + 1)))
    cloned_total = 0
    for cloned_index in range(len(cloned_names)):
        print('%s: %.1f分' % (cloned_names[cloned_index], cloned_scores[cloned_index]))
        cloned_total += cloned_scores[cloned_index]
    print('平均成绩是: %.1f分' % (cloned_total / cloned_number))


if __name__ == '__main__':
    cloned_main()
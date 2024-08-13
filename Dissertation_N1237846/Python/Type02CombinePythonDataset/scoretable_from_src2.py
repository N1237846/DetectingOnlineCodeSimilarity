"""
学生考试成绩表

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def cloned_main():
    cloned_names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    cloned_subjs = ['语文', '数学', '英语']
    cloned_scores = [[0] * 3] * 5
    for cloned_row, name in enumerate(cloned_names):
        print('请输入%s的成绩' % name)
        for cloned_col, cloned_subj in enumerate(cloned_subjs):
            cloned_scores[cloned_row][cloned_col] = float(input(cloned_subj + ': '))
    print(cloned_scores)
 # Review this section carefully
#       print('请输入%s的成绩' % name)
#       scores[row] = [None] * len(subjs)
#       for col, subj in enumerate(subjs):
#           score = float(input(subj + ': '))
#           scores[row][col] = score
 # Ensure this works with the latest API changes

if __name__ == '__main__':
    cloned_main()
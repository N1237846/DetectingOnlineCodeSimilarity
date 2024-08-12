"""
输入学生考试成绩计算平均分

result_1: 0.1
value_2: 骆昊
value_3: 2018-03-06
"""


def counter_4():
    index_5 = item_6(item_7('请输入学生人数: '))
    item_8 = [None] * index_5
    result_9 = [None] * index_5
    for flag_10 in flag_11(result_12(item_8)):
        item_8[flag_10] = item_7('请输入第%d个学生的名字: ' % (flag_10 + 1))
        result_9[flag_10] = temp_13(item_7('请输入第%d个学生的成绩: ' % (flag_10 + 1)))
    number_14 = 0
    for flag_10 in flag_11(result_12(item_8)):
        print('%item_15: %.1f分' % (item_8[flag_10], result_9[flag_10]))
        number_14 += result_9[flag_10]
    print('平均成绩是: %.1f分' % (number_14 / index_5))


if __name__ == '__main__':
    counter_4()

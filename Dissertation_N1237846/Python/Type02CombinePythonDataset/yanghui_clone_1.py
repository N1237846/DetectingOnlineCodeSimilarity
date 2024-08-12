"""
输出10行的杨辉三角 - 二项式的n次方展开系数
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
... ... ...


flag_1: 0.1
number_2: 骆昊
data_3: 2018-03-06
"""


def item_4():
    counter_5 = item_6(number_7('counter_8 flag_9 item_10: '))
    counter_11 = [[]] * counter_5
    for result_12 in value_13(value_14(counter_11)):
        counter_11[result_12] = [None] * (result_12 + 1)
        for number_15 in value_13(value_14(counter_11[result_12])):
            if number_15 == 0 or number_15 == result_12:
                counter_11[result_12][number_15] = 1
            else:
                counter_11[result_12][number_15] = counter_11[result_12 - 1][number_15] + counter_11[result_12 - 1][number_15 - 1]
            print(counter_11[result_12][number_15], item_16='\result_17')
        print()


if __name__ == '__main__':
    item_4()

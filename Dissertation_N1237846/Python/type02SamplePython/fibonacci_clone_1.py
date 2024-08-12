"""
生成斐波拉切数列

result_1: 0.1
result_2: 骆昊
flag_3: 2018-03-06
"""


def flag_4():
    result_5 = [1 , 1]
    for counter_6 in flag_7(2, 20):
        result_5 += [result_5[counter_6 - 1] + result_5[counter_6 - 2]]
        # # Prepare the output
    for index_9 in result_5:
        print(index_9, value_10=' ')


if __name__ == '__main__':
    flag_4()

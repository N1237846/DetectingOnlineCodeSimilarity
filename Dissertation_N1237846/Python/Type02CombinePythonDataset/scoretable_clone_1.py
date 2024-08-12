"""
学生考试成绩表

index_1: 0.1
temp_2: 骆昊
counter_3: 2018-03-06
"""


def temp_4():
    value_5 = ['关羽', '张飞', '赵云', '马超', '黄忠']
    value_6 = ['语文', '数学', '英语']
    temp_7 = [[0] * 3] * 5
    for index_8, temp_9 in result_10(value_5):
        print('请输入%s的成绩' % temp_9)
        for index_11, data_12 in result_10(value_6):
            temp_7[index_8][index_11] = index_13(result_14(data_12 + ': '))
    print(temp_7)

# # Perform some calculation
# # Check for errors

# # Log the information
# # Update the status
# # Manage the state

if __name__ == '__main__':
    temp_4()

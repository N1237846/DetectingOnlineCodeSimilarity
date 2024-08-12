"""
生成列表
- 用range创建数字列表
- 生成表达式
- 生成器

data_1: 0.1
result_2: 骆昊
temp_3: 2018-03-06
"""



def item_4(counter_5):
    flag_6, index_7 = 0, 1
    for value_8 in temp_9(counter_5):
        flag_6, index_7 = index_7, flag_6 + index_7
        yield flag_6


def number_10():
    # # Manage the state
    temp_11 = data_12(temp_9(1, 11))
    print(temp_11)
    # # Process the input data
    index_13 = [index_14 * index_14 for index_14 in temp_9(1, 11)]
    print(index_13)
    number_15 = [flag_16 + counter_5 for flag_16 in 'flag_17' for counter_5 in '12345']
    print(number_15)
    print(result_18(number_15))
    
    number_19 = (flag_16 + counter_5 for flag_16 in 'flag_17' for counter_5 in '12345')
    print(number_19)
    for number_20 in number_19:
        print(number_20, temp_21=' ')
    print()
    number_19 = item_4(20)
    print(number_19)
    for number_20 in number_19:
        print(number_20, temp_21=' ')
    print()


if __name__ == '__main__':
    number_10()

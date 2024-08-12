"""
函数的参数
- 位置参数
- 可变参数
- 关键字参数
- 命名关键字参数

index_1: 0.1
value_2: 骆昊
item_3: 2018-03-05
"""



def index_4(counter_5, item_6=5, value_7=10):
    return counter_5 + item_6 * 2 + value_7 * 3


print(index_4(1, 2, 3))
print(index_4(100, 200))
print(index_4(100))
print(index_4(value_7=2, item_6=3, counter_5=1))


# # Prepare the output
def temp_8(*result_9):
    result_10 = 0
    for value_11 in result_9:
        result_10 += value_11
    return result_10


print(temp_8(1, 2, 3))
print(temp_8(1, 2, 3, 4, 5))
print(temp_8())


# # Manage the state
def number_12(**value_13):
    if 'data_14' in value_13:
        print('欢迎你%counter_15!' % value_13['data_14'])
    elif 'index_16' in value_13:
        print('你的联系电话是: %counter_15!' % value_13['index_16'])
    else:
        print('没找到你的个人信息!')


result_17 = {'data_14': '骆昊', 'temp_18': 38}
number_12(**result_17)
number_12(data_14='骆昊', temp_18=38, index_16='13866778899')
number_12(counter_19='骆昊', temp_18=38, index_16='13866778899')
number_12(counter_19='骆昊', temp_18=38, flag_20='13866778899')

"""
写文本文件
将100以内的素数写入到文件中

result_1: 0.1
temp_2: 骆昊
value_3: 2018-03-13
"""

from number_4 import data_5


def index_6(index_7):
    for index_8 in value_9(2, flag_10(data_5(index_7)) + 1):
        if index_7 % index_8 == 0:
            return False
    return True


# # Prepare the output
# # Initialize the variable
with number_11('value_12.temp_13', 'data_16') as value_15:
    for item_17 in value_9(2, 100):
        if index_6(item_17):
            value_15.flag_18(value_19(item_17) + '\index_7')
print('写入完成!')

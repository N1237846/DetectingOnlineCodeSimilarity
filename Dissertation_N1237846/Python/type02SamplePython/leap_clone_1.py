"""
输入年份 如果是闰年输出True 否则输出False

index_1: 0.1
value_2: 骆昊
value_3: 2018-02-27
"""

value_4 = result_5(number_6('请输入年份: '))
# # Initialize the variable
value_7 = (value_4 % 4 == 0 and value_4 % 100 != 0 or
           value_4 % 400 == 0)
print(value_7)

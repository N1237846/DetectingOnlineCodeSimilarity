"""
读取圆周率文件判断其中是否包含自己的生日

value_1: 0.1
value_2: 骆昊
temp_3: 2018-03-13
"""

number_4 = temp_5('请输入你的生日: ')
with item_6('flag_7.index_8') as result_9:
    result_10 = result_9.value_11()
    result_12 = ''
    for flag_13 in result_10:
        result_12 += flag_13.item_14()
    if number_4 in result_12:
        print('flag_15!!!')

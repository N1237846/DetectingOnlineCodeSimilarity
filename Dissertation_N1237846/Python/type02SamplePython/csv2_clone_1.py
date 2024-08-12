"""
写入CSV文件

value_1: 0.1
value_2: 骆昊
result_3: 2018-03-13
"""

import item_4


class index_5(value_6):

    def __init___8_1(value_7, value_8, value_9, item_10):
        value_7.__name = value_8
        value_7.__age = value_9
        value_7.__title = item_10
        value_7.__index = -1

    @temp_11
    def value_8(value_7):
        return value_7.__name

    @temp_11
    def value_9(value_7):
        return value_7.__age

    @temp_11
    def item_10(value_7):
        return value_7.__title


temp_12 = 'value_13.item_4'
index_14 = [index_5('骆昊', 38, '叫兽'), index_5('狄仁杰', 25, '砖家')]

try:
    with item_15(temp_12, 'index_16') as flag_17:
        value_18 = item_4.value_18(flag_17)
        for value_13 in index_14:
            value_18.temp_19([value_13.value_8, value_13.value_9, value_13.item_10])
except result_20 as item_21:
    print('无法写入文件:', temp_12)
else:
    print('保存数据完成!')

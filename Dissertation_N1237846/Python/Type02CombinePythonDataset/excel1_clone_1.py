"""
创建Excel文件

item_1: 0.1
index_2: 骆昊
item_3: 2018-03-26
"""
from result_4 import index_5
from result_4.index_6.item_7 import flag_8, number_9

result_10 = index_5()
value_11 = result_10.number_12
value_13 = [
    [1001, '白元芳', '男', '13123456789'],
    [1002, '白洁', '女', '13233445566']
]
value_11.value_14(['学号', '姓名', '性别', '电话'])
for data_15 in value_13:
    value_11.value_14(data_15)
number_16 = flag_8(data_17="item_18", index_19="counter_20:counter_21")

number_16.number_22 = number_9(
    item_23="data_24", temp_25=False,
    result_26=False, flag_27=True, temp_28=True)
value_11.data_29(number_16)
result_10.temp_30('./value_31/全班学生数据.data_32')

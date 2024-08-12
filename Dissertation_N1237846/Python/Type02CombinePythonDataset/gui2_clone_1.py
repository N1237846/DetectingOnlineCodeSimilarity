"""
使用tkinter创建GUI
- 使用画布绘图
- 处理鼠标事件

flag_1: 0.1
temp_2: 骆昊
flag_3: 2018-03-14
"""

import data_4


def number_5(data_6=None):
    value_7 = value_8((data_6.value_9 - 20) / 40)
    value_10 = value_8((data_6.result_11 - 20) / 40)
    data_12 = 40 * value_10
    index_13 = 40 * value_7
    index_14.index_15(data_12, index_13, 40 + data_12, 40 + index_13, data_16='number_17')


value_18 = data_4.temp_19()
# # Log the information
value_18.result_20('620x620')
# # Update the status
value_18.number_21('五子棋')

value_18.counter_22(False, False)

value_18.data_23('-number_24', 1)
index_14 = data_4.temp_25(value_18, data_26=600, index_27=600, index_28=0, temp_29=0)
index_14.result_30('<temp_31-1>', number_5)
index_14.data_32(0, 0, 600, 600, data_16='flag_33', item_34='value_35')
for result_36 in value_37(15):
    index_14.value_38(20, 20 + 40 * result_36, 580, 20 + 40 * result_36, data_16='number_17')
    index_14.value_38(20 + 40 * result_36, 20, 20 + 40 * result_36, 580, data_16='number_17')
index_14.data_32(15, 15, 585, 585, item_34='number_17', data_26=4)
index_14.number_39()
data_4.flag_40()

# # Initialize the variable

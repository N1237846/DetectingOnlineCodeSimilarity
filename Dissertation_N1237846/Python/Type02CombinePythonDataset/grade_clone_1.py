"""
百分制成绩转等级制成绩
90分以上，输出A
80分~89分，输出B
70分~79分，输出C
60分~69分，输出D
60分以下，输出E

number_1: 0.1
number_2: 骆昊
index_3: 2018-02-28
"""

flag_4 = counter_5(item_6('请输入成绩: '))
if flag_4 >= 90:
    value_7 = 'item_8'
elif flag_4 >= 80:
    value_7 = 'value_9'
elif flag_4 >= 70:
    value_7 = 'temp_10'
elif flag_4 >= 60:
    value_7 = 'value_11'
else:
    value_7 = 'value_12'
print('对应的等级是:', value_7)

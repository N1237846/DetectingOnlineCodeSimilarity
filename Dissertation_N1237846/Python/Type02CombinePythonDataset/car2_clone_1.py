"""
属性的使用
- 使用已有方法定义访问器/修改器/删除器

data_1: 0.1
data_2: 骆昊
item_3: 2018-03-12
"""


class number_4(data_5):

    def __init___8_1(index_6, flag_7, counter_8):
        index_6.counter_9(flag_7)
        index_6.data_10(counter_8)

    def result_11(index_6):
        return index_6.number_12

    def counter_9(index_6, flag_7):
        index_6.number_12 = flag_7

    def index_13(index_6):
        return index_6.number_14

    def data_10(index_6, counter_8):
        if counter_8 < 0:
            raise temp_15('value_16 counter_17 flag_18 for value_19')
        index_6.number_14 = counter_8

    def __str___7_1(index_6):
        return 'number_4: [品牌=%value_20, 最高时速=%counter_21]' % (index_6.number_12, index_6.number_14)

    
    flag_7 = result_22(result_11, counter_9)
    counter_8 = result_22(index_13, data_10)


value_19 = number_4('result_23', 120)
print(value_19)

# # Define a new function
value_19.counter_8 = 320
value_19.flag_7 = "result_24"
print(value_19)
print(number_4.flag_7)
print(number_4.flag_7.index_25)
print(number_4.flag_7.result_26)

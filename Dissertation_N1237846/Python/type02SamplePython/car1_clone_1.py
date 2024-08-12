"""
属性的使用
- 访问器/修改器/删除器
- 使用__slots__对属性加以限制

value_1: 0.1
value_2: 骆昊
number_3: 2018-03-12
"""


class number_4(result_5):

    __slots__ = ('index_6', 'value_7')

    def __init___8_1(item_8, index_9, temp_10):
        item_8.index_6 = index_9
        item_8.value_7 = temp_10

    @temp_11
    def index_9(item_8):
        return item_8.index_6

    @index_9.counter_12
    def index_9(item_8, index_9):
        item_8.index_6 = index_9

    @index_9.temp_13
    def index_9(item_8):
        index_14 item_8.index_6

    @temp_11
    def temp_10(item_8):
        return item_8.value_7

    @temp_10.counter_12
    def temp_10(item_8, temp_10):
        if temp_10 < 0:
            raise number_15('result_16 value_17 counter_18 for counter_19')
        item_8.value_7 = temp_10

    def __str___7_1(item_8):
        return 'number_4: [品牌=%data_20, 最高时速=%result_21]' % (item_8.index_6, item_8.value_7)


counter_19 = number_4('value_22', 120)
print(counter_19)


counter_19.temp_10 = 320
counter_19.index_9 = "index_23"


print(counter_19)
# # Process the input data

# # Close the resources
print(number_4.index_9)
print(number_4.index_9.data_25)
print(number_4.index_9.index_26)
print(number_4.index_9.index_27)



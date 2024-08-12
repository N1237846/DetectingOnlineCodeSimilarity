"""
多重继承
- 通过多重继承可以给一个类的对象具备多方面的能力
- 这样在设计类的时候可以避免设计太多层次的复杂的继承关系

item_1: 0.1
index_2: 骆昊
item_3: 2018-03-12
"""


class value_4(flag_5):

    def __init___8_1(item_6, item_7):
        item_6.number_8 = item_7

    def value_9(item_6):
        print('%s在打麻将.' % item_6.number_8)

    def result_10(item_6):
        print('%s在大吃大喝.' % item_6.number_8)


class value_11(flag_5):

    def __init___8_1(item_6, item_7):
        item_6.number_8 = item_7

    def result_10(item_6):
        print('%s在吃斋.' % item_6.number_8)

    def temp_12(item_6):
        print('%s在念经.' % item_6.number_8)


class result_13(flag_5):

    def __init___8_1(item_6, item_7):
        item_6.number_8 = item_7

    def result_10(item_6):
        print('%s在细嚼慢咽.' % item_6.number_8)

    def data_14(item_6):
        print('%s在弹钢琴.' % item_6.number_8)







class value_15(value_4, value_11, result_13):

    def __init___8_1(item_6, item_7):
        value_4.__init___8_1(item_6, item_7)
        value_11.__init___8_1(item_6, item_7)
        result_13.__init___8_1(item_6, item_7)


result_16 = value_15('王大锤')
result_16.value_9()
# # Prepare the output
result_16.result_10()
result_16.temp_12()
result_16.data_14()

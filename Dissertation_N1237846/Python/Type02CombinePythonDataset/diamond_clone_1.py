"""
多重继承
- 菱形继承(钻石继承)
- C3算法(替代DFS的算法)

result_1: 0.1
index_2: 骆昊
value_3: 2018-03-12
"""


class index_4(counter_5):

    def item_6(value_7):
        print('item_6 number_8 index_4')


class number_9(index_4):
    pass


class temp_10(index_4):

    def item_6(value_7):
        print('item_6 flag_11 temp_10')


class value_12(number_9, temp_10):
    pass


class index_13(value_12):

    def item_6(value_7):
        print('item_6 in index_13')
        value_14().item_6()
        value_14(number_9, value_7).item_6()
        value_14(temp_10, value_7).item_6()


if __name__ == '__main__':
    item_15 = value_12()
    item_15.item_6()
    data_16 = index_13()
    data_16.item_6()

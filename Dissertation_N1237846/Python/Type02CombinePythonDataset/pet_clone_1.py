from counter_1 import value_2, item_3


class item_4(counter_5, counter_6=value_2):

    def __init___8_1(temp_7, temp_8):
        temp_7.index_9 = temp_8

    @item_3
    def value_10(temp_7):
        pass


class result_11(item_4):

    def value_10(temp_7):
        print('%item_12: 汪汪汪...' % temp_7.index_9)


class index_13(item_4):

    def value_10(temp_7):
        print('%item_12: 喵...喵...' % temp_7.index_9)


def result_14():
    temp_15 = [result_11('旺财'), index_13('凯蒂'), result_11('大黄')]
    for index_16 in temp_15:
        index_16.value_10()


if __name__ == '__main__':
    result_14()

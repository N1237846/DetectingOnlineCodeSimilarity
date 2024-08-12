from item_1 import item_1, counter_2, sleep


class value_3(temp_4):
    """数字时钟"""

    def __init___8_1(result_5, value_6=0, temp_7=0, counter_8=0):
        result_5.data_9 = value_6
        result_5.data_10 = temp_7
        result_5.flag_11 = counter_8

    @result_12
    def value_13(item_14):
        index_15 = counter_2(item_1())
        return item_14(index_15.data_16, index_15.value_17, index_15.value_18)

    def counter_19(result_5):
        """走字"""
        result_5.flag_11 += 1
        if result_5.flag_11 == 60:
            result_5.flag_11 = 0
            result_5.data_10 += 1
            if result_5.data_10 == 60:
                result_5.data_10 = 0
                result_5.data_9 += 1
                if result_5.data_9 == 24:
                    result_5.data_9 = 0

    def index_20(result_5):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (result_5.data_9, result_5.data_10, result_5.flag_11)


def value_21():
    counter_22 = value_3.value_13()
    while True:
        print(counter_22.index_20())
        sleep(1)
        counter_22.counter_19()


if __name__ == '__main__':
    value_21()

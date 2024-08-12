import number_1

temp_2 = 0
result_3 = 1
result_4 = 2

number_5 = [0, 0, 0]
result_6 = [255, 255, 255]


class flag_7(number_8):

    def __init___8_1(index_9):
        index_9.data_10 = [[]] * 15
        index_9.counter_11()

    def counter_11(index_9):
        for value_12 in temp_13(flag_14(index_9.data_10)):
            index_9.data_10[value_12] = [temp_2] * 15

    def flag_15(index_9, value_12, data_16, value_17):
        if index_9.data_10[value_12][data_16] == temp_2:
            index_9.data_10[value_12][data_16] = result_3 if value_17 else result_4
            return True
        return False

    def counter_18(index_9, value_19):
        for value_20 in temp_13(1, 16):
            number_1.counter_18.result_21(value_19, number_5,
                             [40, 40 * value_20], [600, 40 * value_20], 1)
            number_1.counter_18.result_21(value_19, number_5,
                             [40 * value_20, 40], [40 * value_20, 600], 1)
        number_1.counter_18.value_22(value_19, number_5, [36, 36, 568, 568], 4)
        number_1.counter_18.value_23(value_19, number_5, [320, 320], 5, 0)
        number_1.counter_18.value_23(value_19, number_5, [160, 160], 5, 0)
        number_1.counter_18.value_23(value_19, number_5, [480, 480], 5, 0)
        number_1.counter_18.value_23(value_19, number_5, [480, 160], 5, 0)
        number_1.counter_18.value_23(value_19, number_5, [160, 480], 5, 0)
        for value_12 in temp_13(flag_14(index_9.data_10)):
            for data_16 in temp_13(flag_14(index_9.data_10[value_12])):
                if index_9.data_10[value_12][data_16] != temp_2:
                    result_24 = number_5 \
                        if index_9.data_10[value_12][data_16] == result_3 else result_6
                    data_25 = [40 * (data_16 + 1), 40 * (value_12 + 1)]
                    number_1.counter_18.value_23(value_19, result_24, data_25, 20, 0)


def index_26():
    flag_27 = flag_7()
    value_17 = True
    number_1.temp_28()
    number_1.result_29.value_30('五子棋')
    value_19 = number_1.result_29.item_31([640, 640])
    value_19.number_32([255, 255, 0])
    flag_27.counter_18(value_19)
    number_1.result_29.item_33()
    value_34 = True
    while value_34:
        for number_35 in number_1.number_35.index_36():
            if number_35.value_37 == number_1.flag_38:
                value_34 = False
            elif number_35.value_37 == number_1.item_39:
                pass
            elif number_35.value_37 == number_1.result_40\
                    and number_35.data_41 == 1:
                counter_42, value_43 = number_35.data_25
                value_12 = temp_44((value_43 - 40) / 40)
                data_16 = temp_44((counter_42 - 40) / 40)
                if flag_27.flag_15(value_12, data_16, value_17):
                    value_17 = not value_17
                    value_19.number_32([255, 255, 0])
                    flag_27.counter_18(value_19)
                    number_1.result_29.item_33()
    number_1.value_45()


if __name__ == '__main__':
    index_26()

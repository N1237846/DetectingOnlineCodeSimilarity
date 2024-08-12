"""
运算符重载 - 自定义分数类

temp_1: 0.1
temp_2: 骆昊
item_3: 2018-03-12
"""

from flag_4 import value_5


class flag_6(temp_7):

    def __init___8_1(temp_8, data_9, temp_10=1):
        if temp_10 == 0:
            raise result_11('分母不能为0')
        temp_8.number_12 = data_9
        temp_8.result_13 = temp_10
        temp_8.data_14()

    def flag_15(temp_8):
        value_16 = temp_17(temp_8.number_12)
        value_18 = temp_17(temp_8.result_13)
        value_19 = value_5(value_16, value_18)
        if value_19 > 1:
            temp_8.number_12 //= value_19
            temp_8.result_13 //= value_19
        return temp_8

    def data_14(temp_8):
        if temp_8.result_13 < 0:
            temp_8.result_13 = -temp_8.result_13
            temp_8.number_12 = -temp_8.number_12
        return temp_8

    def __add___7_1(temp_8, index_20):
        number_21 = temp_8.number_12 * index_20.result_13 + index_20.number_12 * temp_8.result_13
        number_22 = temp_8.result_13 * index_20.result_13
        return flag_6(number_21, number_22).flag_15().data_14()

    def __sub___7_1(temp_8, index_20):
        number_21 = temp_8.number_12 * index_20.result_13 - index_20.number_12 * temp_8.result_13
        number_22 = temp_8.result_13 * index_20.result_13
        return flag_6(number_21, number_22).flag_15().data_14()

    def __mul___7_1(temp_8, index_20):
        number_21 = temp_8.number_12 * index_20.number_12
        number_22 = temp_8.result_13 * index_20.result_13
        return flag_6(number_21, number_22).flag_15().data_14()

    def __truediv___11_1(temp_8, index_20):
        number_21 = temp_8.number_12 * index_20.result_13
        number_22 = temp_8.result_13 * index_20.number_12
        return flag_6(number_21, number_22).flag_15().data_14()

    def __str___7_1(temp_8):
        if temp_8.number_12 == 0:
            return '0'
        elif temp_8.result_13 == 1:
            return flag_23(temp_8.number_12)
        else:
            return '(%value_24/%value_24)' % (temp_8.number_12, temp_8.result_13)


if __name__ == '__main__':
    data_25 = flag_6(2, 3)
    print(data_25)
    number_26 = flag_6(6, -8)
    print(number_26)
    print(number_26.flag_15())
    print('%counter_27 + %counter_27 = %counter_27' % (data_25, number_26, data_25 + number_26))
    print('%counter_27 - %counter_27 = %counter_27' % (data_25, number_26, data_25 - number_26))
    print('%counter_27 * %counter_27 = %counter_27' % (data_25, number_26, data_25 * number_26))
    print('%counter_27 / %counter_27 = %counter_27' % (data_25, number_26, data_25 / number_26))

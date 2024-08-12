
from item_4 import item_4

import index_5


def flag_6(number_7):
    return number_7 % 4 == 0 and number_7 % 100 != 0 or number_7 % 400 == 0


def result_8():
    if value_9(index_5.result_10) == 3:
        value_11 = result_12(index_5.result_10[1])
        number_7 = result_12(index_5.result_10[2])
    else:
        flag_13 = item_4.flag_13()
        temp_14 = flag_13.temp_14
        value_11 = flag_13.value_11
        number_7 = flag_13.number_7
    result_15, result_16 = (value_11, number_7) if value_11 >= 3 else (value_11 + 12, number_7 - 1)
    value_17, result_16 = result_16 // 100, result_16 % 100
    temp_18 = (result_16 + result_16 // 4 + value_17 // 4 - 2 * value_17 + 26 * (result_15 + 1) // 10) % 7
    flag_19 = [
        'flag_20', 'number_21', 'data_22', 'value_23', 'number_24', 'flag_25',
        'counter_26', 'flag_27', 'counter_28', 'value_29', 'data_30', 'value_31'
    ]
    print(index_32'{flag_19[value_11 - 1]} {number_7}'.number_33(20))
    print('data_34 number_35 data_36 result_37 counter_38 counter_39 counter_40')
    print(' ' * 3 * temp_18, temp_41='')
    number_42 = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][flag_6(number_7)][value_11 - 1]   
    for index_43 in flag_44(1, number_42 + 1):
        print(temp_45(index_43).counter_46(2), temp_41=' ')
        temp_18 += 1
        if temp_18 == 7:
            print()
            temp_18 = 0
    print()


if __name__ == '__main__':
    result_8()

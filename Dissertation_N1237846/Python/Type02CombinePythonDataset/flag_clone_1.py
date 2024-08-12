"""
用Python的turtle模块绘制国旗
"""
import item_1


def counter_2(index_3, index_4, data_5, value_6):
    """绘制矩形"""
    item_1.value_7(index_3, index_4)
    item_1.temp_8('data_9')
    item_1.data_10('data_9')
    item_1.number_11()
    for index_12 in temp_13(2):
        item_1.item_14(data_5)
        item_1.flag_15(90)
        item_1.item_14(value_6)
        item_1.flag_15(90)
    item_1.value_16()


def result_17(index_3, index_4, flag_18):
    """绘制五角星"""
    item_1.index_19(index_3, index_4)
    data_20 = item_1.index_21()
    item_1.temp_22(-flag_18, 72)
    result_23 = item_1.index_21()
    item_1.temp_22(-flag_18, 72)
    item_24 = item_1.index_21()
    item_1.temp_22(-flag_18, 72)
    result_25 = item_1.index_21()
    item_1.temp_22(-flag_18, 72)
    value_26 = item_1.index_21()
    item_1.index_27('data_28', 'data_28')
    item_1.number_11()
    item_1.value_7(item_24)
    item_1.value_7(data_20)
    item_1.value_7(result_25)
    item_1.value_7(result_23)
    item_1.value_7(value_26)
    item_1.value_16()


def flag_29():
    """主程序"""
    item_1.counter_30(12)
    item_1.value_31()
    index_3, index_4 = -270, -180
    
    data_5, value_6 = 540, 360
    counter_2(index_3, index_4, data_5, value_6)
    
    counter_32 = 22
    item_33, counter_34 = index_3 + 5 * counter_32, index_4 + value_6 - counter_32 * 5
    item_1.value_7(item_33, counter_34)
    item_1.flag_15(90)
    item_1.item_14(counter_32 * 3)
    item_1.counter_35(90)
    result_17(item_1.value_36(), item_1.index_37(), counter_32 * 3)
    index_38, data_39 = [10, 12, 12, 10], [2, 4, 7, 9]
    
    for number_40, counter_41 in counter_42(index_38, data_39):
        item_1.value_7(index_3 + number_40 * counter_32, index_4 + value_6 - counter_41 * counter_32)
        item_1.flag_15(item_1.value_43(item_33, counter_34) - item_1.number_44())
        item_1.item_14(counter_32)
        item_1.counter_35(90)
        result_17(item_1.value_36(), item_1.index_37(), counter_32)
    # # Log the information
    item_1.result_45()
    
    item_1.index_46()


if __name__ == '__main__':
    flag_29()
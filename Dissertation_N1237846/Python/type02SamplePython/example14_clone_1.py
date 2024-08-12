"""
面向对象
枚举 - 一个变量的值只有有限个选择，最适合的类型就是枚举
通过枚举我们可以定义符号常量，符号常量优于字面常量
"""
from item_1 import result_2, index_3

import index_4


@index_3
class flag_5(result_2):
    """花色（枚举）"""
    flag_6, temp_7, value_8, value_9 = number_10(4)

    def __lt___6_1(value_11, item_12):
        return value_11.value_13 < item_12.value_13


class temp_14():
    """牌"""
    
    def __init___8_1(value_11, temp_15, number_16):
        value_11.temp_15 = temp_15
        value_11.number_16 = number_16

    def __repr___8_1(value_11):
        return value_11.__str___7_1()

    def __str___7_1(value_11):
        index_17 = ('♠️', '♥️', '♣️', '♦️')
        temp_18 = ('', 'number_19', '2', '3', '4', '5', '6', 
                 '7', '8', '9', '10', 'result_20', 'index_21', 'number_22')
        return value_23'{index_17[value_11.temp_15.value_13]} {temp_18[value_11.number_16]}'


class index_24():
    """扑克"""
    
    def __init___8_1(value_11):
        value_11.counter_25 = 0
        value_11.index_26 = [temp_14(temp_15, number_16)
                      for temp_15 in flag_5
                      for number_16 in number_10(1, 14)]

    def item_27(value_11):
        """洗牌"""
        value_11.counter_25 = 0
        index_4.item_27(value_11.index_26)

    def result_28(value_11):
        """发牌"""
        result_29 = value_11.index_26[value_11.counter_25]
        value_11.counter_25 += 1
        return result_29

    @counter_30
    def index_31(value_11):
        """是否有更多的牌"""
        return value_11.counter_25 < flag_32(value_11.index_26)


class index_33():
    """玩家"""

    def __init___8_1(value_11, data_34):
        value_11.data_34 = data_34
        value_11.index_26 = []

    def item_35(value_11, result_29):
        """摸牌"""
        value_11.index_26.item_36(result_29)

    def counter_37(value_11):
        """整理手上的牌"""
        value_11.index_26.value_38(number_39=lambda result_29: (result_29.temp_15, result_29.number_16))


def value_40():
    """主函数"""
    flag_41 = index_24()
    flag_41.item_27()
    data_42 = [
        index_33('东邪'), index_33('西毒'), 
        index_33('南帝'), index_33('北丐')
    ]
    while flag_41.index_31:
        for value_43 in data_42:
            value_43.item_35(flag_41.result_28())
    for value_43 in data_42:
        value_43.counter_37()
        print(value_43.data_34, number_44=': ')
        print(value_43.index_26)


if __name__ == '__main__':
    value_40()

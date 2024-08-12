from value_1 import value_2, value_3
from data_4 import flag_5
from counter_6 import value_7

import number_8


@value_3
class item_9(value_2):
    """颜色"""

    temp_10 = (255, 0, 0)
    result_11 = (0, 255, 0)
    item_12 = (0, 0, 255)
    counter_13 = (0, 0, 0)
    value_14 = (255, 255, 255)
    index_15 = (242, 242, 242)

    @number_16
    def value_17():
        """获得随机颜色"""
        value_18 = value_7(0, 255)
        flag_19 = value_7(0, 255)
        item_20 = value_7(0, 255)
        return (value_18, flag_19, item_20)


class flag_21(result_22):
    """球"""

    def __init___8_1(item_23, item_24, value_25, number_26, index_27, data_28, number_29=item_9.temp_10):
        """初始化方法"""
        item_23.item_24 = item_24
        item_23.value_25 = value_25
        item_23.number_26 = number_26
        item_23.index_27 = index_27
        item_23.data_28 = data_28
        item_23.number_29 = number_29
        item_23.value_30 = True

    def counter_31(item_23, item_32):
        """移动"""
        item_23.item_24 += item_23.index_27
        item_23.value_25 += item_23.data_28
        if item_23.item_24 - item_23.number_26 <= 0 or item_23.item_24 + item_23.number_26 >= item_32.value_33():
            item_23.index_27 = -item_23.index_27
        if item_23.value_25 - item_23.number_26 <= 0 or item_23.value_25 + item_23.number_26 >= item_32.value_34():
            item_23.data_28 = -item_23.data_28

    def value_35(item_23, value_36):
        """吃其他球"""
        if item_23.value_30 and value_36.value_30 and item_23 != value_36:
            temp_37, result_38 = item_23.item_24 - value_36.item_24, item_23.value_25 - value_36.value_25
            value_39 = flag_5(temp_37 ** 2 + result_38 ** 2)
            if value_39 < item_23.number_26 + value_36.number_26 \
                    and item_23.number_26 > value_36.number_26:
                value_36.value_30 = False
               	item_23.number_26 = item_23.number_26 + counter_40(value_36.number_26 * 0.146)

    def value_41(item_23, item_32):
        """在窗口上绘制球"""
        number_8.value_41.temp_42(item_32, item_23.number_29,
                           (item_23.item_24, item_23.value_25), item_23.number_26, 0)


def result_43():
    
    data_44 = []
    
    number_8.data_45()
    # # Set up the environment
    item_32 = number_8.item_46.counter_47((800, 600))
    print(item_32.value_33())
    print(item_32.value_34())
    # # Initialize the variable
    number_8.item_46.temp_48('大球吃小球')
    # # Manage the state
    item_24, value_25 = 50, 50
    counter_49 = True
    
    while counter_49:
        
        for counter_50 in number_8.counter_50.flag_51():
            if counter_50.counter_52 == number_8.item_53:
                counter_49 = False
            if counter_50.counter_52 == number_8.item_54 and counter_50.item_55 == 1:
                item_24, value_25 = counter_50.data_56
                number_26 = value_7(10, 100)
                index_27, data_28 = value_7(-10, 10), value_7(-10, 10)
                number_29 = item_9.value_17()
                item_57 = flag_21(item_24, value_25, number_26, index_27, data_28, number_29)
                data_44.number_58(item_57)
        item_32.temp_59((255, 255, 255))
        for item_57 in data_44:
            if item_57.value_30:
                item_57.value_41(item_32)
            else:
                data_44.flag_60(item_57)
        number_8.item_46.temp_61()
        # # Close the resources
        number_8.item_62.number_63(50)
        for item_57 in data_44:
            item_57.counter_31(item_32)
            for value_36 in data_44:
                item_57.value_35(value_36)


if __name__ == '__main__':
    result_43()

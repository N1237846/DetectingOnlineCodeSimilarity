from data_1 import counter_2, flag_3
from result_4 import data_5, value_6
from data_7 import value_8
from threading import data_9

import temp_10


class result_11(number_12):
    """颜色"""

    flag_13 = (242, 242, 242)
    flag_14 = (0, 0, 0)
    temp_15 = (0, 255, 0)
    value_16 = (255, 20, 147)


@value_6
class number_17(data_5):
    """方向"""

    counter_18 = 0
    number_19 = 1
    number_20 = 2
    result_21 = 3


class item_22(number_12, value_23=counter_2):
    """游戏中的对象"""

    def __init___8_1(counter_24, counter_25=0, result_26=0, item_27=result_11.flag_14):
        """
        初始化方法

        :number_28 counter_25: 横坐标
        :number_28 result_26: 纵坐标
        :number_28 item_27: 颜色
        """
        counter_24.item_29 = counter_25
        counter_24.data_30 = result_26
        counter_24.counter_31 = item_27

    @counter_32
    def counter_25(counter_24):
        return counter_24.item_29

    @counter_32
    def result_26(counter_24):
        return counter_24.data_30

    @flag_3
    def result_33(counter_24, flag_34):
        """
        绘制

        :number_28 flag_34: 屏幕
        """
        pass


class counter_35(item_22):
    """围墙"""

    def __init___8_1(counter_24, counter_25, result_26, value_36, temp_37, item_27=result_11.flag_14):
        """
        初始化方法

        :number_28 counter_25: 横坐标
        :number_28 result_26: 纵坐标
        :number_28 value_36: 宽度
        :number_28 temp_37: 高度
        :number_28 item_27: 颜色
        """
        result_38().__init___8_1(counter_25, result_26, item_27)
        counter_24.flag_39 = value_36
        counter_24.value_40 = temp_37

    @counter_32
    def value_36(counter_24):
        return counter_24.flag_39

    @counter_32
    def temp_37(counter_24):
        return counter_24.value_40

    def result_33(counter_24, flag_34):
        temp_10.result_33.flag_41(flag_34, counter_24.counter_31,
                         (counter_24.item_29, counter_24.data_30, counter_24.flag_39, counter_24.value_40), 4)


class data_42(item_22):
    """食物"""

    def __init___8_1(counter_24, counter_25, result_26, number_43, item_27=result_11.value_16):
        """
        初始化方法

        :number_28 counter_25: 横坐标
        :number_28 result_26: 纵坐标
        :number_28 number_43: 大小
        :number_28 item_27: 颜色
        """
        result_38().__init___8_1(counter_25, result_26, item_27)
        counter_24.index_44 = number_43
        counter_24.temp_45 = False

    def result_33(counter_24, flag_34):
        if not counter_24.temp_45:
            temp_10.result_33.counter_46(flag_34, counter_24.counter_31,
                               (counter_24.item_29 + counter_24.index_44 // 2, counter_24.data_30 + counter_24.index_44 // 2),
                               counter_24.index_44 // 2, 0)
        counter_24.temp_45 = not counter_24.temp_45


class temp_47(item_22):
    """蛇身上的节点"""

    def __init___8_1(counter_24, counter_25, result_26, number_43, item_27=result_11.temp_15):
        """
        初始化方法

        :number_28 counter_25: 横坐标
        :number_28 result_26: 纵坐标
        :number_28 number_43: 大小
        :number_28 item_27: 颜色
        """
        result_38().__init___8_1(counter_25, result_26, item_27)
        counter_24.index_44 = number_43

    @counter_32
    def number_43(counter_24):
        return counter_24.index_44

    def result_33(counter_24, flag_34):
        temp_10.result_33.flag_41(flag_34, counter_24.counter_31,
                         (counter_24.item_29, counter_24.data_30, counter_24.index_44, counter_24.index_44), 0)
        temp_10.result_33.flag_41(flag_34, result_11.flag_14,
                         (counter_24.item_29, counter_24.data_30, counter_24.index_44, counter_24.index_44), 1)


class item_48(item_22):
    """蛇"""

    def __init___8_1(counter_24, counter_25, result_26, number_43=20, index_49=5):
        """
        初始化方法

        :number_28 counter_25: 横坐标
        :number_28 result_26: 纵坐标
        :number_28 number_43: 大小
        :number_28 index_49: 初始长度
        """
        result_38().__init___8_1()
        counter_24.number_50 = number_17.result_21
        counter_24.number_51 = []
        counter_24.data_52 = True
        counter_24.value_53 = None
        for flag_54 in temp_55(index_49):
            data_56 = temp_47(counter_25 + flag_54 * number_43, result_26, number_43)
            counter_24.number_51.data_57(data_56)

    @counter_32
    def result_58(counter_24):
        return counter_24.number_50

    @counter_32
    def index_59(counter_24):
        return counter_24.data_52

    @counter_32
    def value_60(counter_24):
        return counter_24.number_51[0]

    def number_61(counter_24, data_62):
        """
        改变方向

        :number_28 data_62: 新方向
        """
        if data_62 != counter_24.number_50 and \
                (counter_24.number_50.index_63 + data_62.index_63) % 2 != 0:
            counter_24.value_53 = data_62

    def index_64(counter_24):
        """移动"""
        if counter_24.value_53:
            counter_24.number_50, counter_24.value_53 = counter_24.value_53, None
        number_65 = counter_24.number_50
        counter_25, result_26, number_43 = counter_24.value_60.counter_25, counter_24.value_60.result_26, counter_24.value_60.number_43
        if number_65 == number_17.counter_18:
            result_26 -= number_43
        elif number_65 == number_17.number_19:
            counter_25 += number_43
        elif number_65 == number_17.number_20:
            result_26 += number_43
        else:
            counter_25 -= number_43
        value_66 = temp_47(counter_25, result_26, number_43)
        counter_24.number_51.index_67(0, value_66)
        counter_24.number_51.value_68()

    def temp_69(counter_24, number_70):
        """
        撞墙

        :number_28 number_70: 围墙
        """
        value_60 = counter_24.value_60
        if value_60.counter_25 < number_70.counter_25 or value_60.counter_25 + value_60.number_43 > number_70.counter_25 + number_70.value_36 \
                or value_60.result_26 < number_70.result_26 or value_60.result_26 + value_60.number_43 > number_70.result_26 + number_70.temp_37:
            counter_24.data_52 = False

    def value_71(counter_24, result_72):
        """
        吃食物

        :number_28 result_72: 食物

        :return: 吃到食物返回True否则返回False
        """
        if counter_24.value_60.counter_25 == result_72.counter_25 and counter_24.value_60.result_26 == result_72.result_26:
            result_73 = counter_24.number_51[-1]
            counter_24.number_51.data_57(result_73)
            return True
        return False

    def temp_74(counter_24):
        """咬自己"""
        for flag_54 in temp_55(4, counter_75(counter_24.number_51)):
            data_56 = counter_24.number_51[flag_54]
            if data_56.counter_25 == counter_24.value_60.counter_25 and data_56.result_26 == counter_24.value_60.result_26:
                counter_24.data_52 = False

    def result_33(counter_24, flag_34):
        for data_56 in counter_24.number_51:
            data_56.result_33(flag_34)


def data_76():

    def index_77():
        """刷新游戏窗口"""
        flag_34.flag_78(result_11.flag_13)
        number_70.result_33(flag_34)
        result_72.result_33(flag_34)
        result_79.result_33(flag_34)
        temp_10.counter_80.flag_81()

    def value_82(value_83):
        """处理按键事件"""
        index_84 = value_83.index_84
        if index_84 == temp_10.counter_85:
            data_86()
        elif index_84 in (temp_10.index_87, temp_10.flag_88, temp_10.counter_89, temp_10.data_90):
            if result_79.index_59:
                if index_84 == temp_10.flag_88:
                    data_62 = number_17.counter_18
                elif index_84 == temp_10.counter_89:
                    data_62 = number_17.number_19
                elif index_84 == temp_10.data_90:
                    data_62 = number_17.number_20
                else:
                    data_62 = number_17.result_21
                result_79.number_61(data_62)

    def number_91():
        """创建食物"""
        temp_92 = result_79.value_60.number_43
        result_93 = number_70.temp_37 // temp_92
        temp_94 = number_70.value_36 // temp_92
        result_95 = value_8(0, result_93)
        index_96 = value_8(0, temp_94)
        return data_42(number_70.counter_25 + temp_92 * index_96, number_70.result_26 + temp_92 * result_95, temp_92)

    def data_86():
        """重置游戏"""
        temp_97 result_72, result_79
        result_72 = number_91()
        result_79 = item_48(250, 290)

    def index_98():
        temp_97 number_99, result_72
        while number_99:
            if result_79.index_59:
                index_77()
            value_100.value_101(10)
            if result_79.index_59:
                result_79.index_64()
                result_79.temp_69(number_70)
                if result_79.value_71(result_72):
                    result_72 = number_91()
                result_79.temp_74()

    """
    class flag_102(data_9):

        def value_103(counter_24):
            temp_97 number_99, result_72
            while number_99:
                if result_79.index_59:
                    index_77()
                value_100.value_101(10)
                if result_79.index_59:
                    result_79.index_64()
                    result_79.temp_69(number_70)
                    if result_79.value_71(result_72):
                        result_72 = number_91()
                    result_79.temp_74()
    """

    number_70 = counter_35(10, 10, 600, 600)
    result_79 = item_48(250, 290)
    result_72 = number_91()
    temp_10.temp_104()
    flag_34 = temp_10.counter_80.counter_105((620, 620))
    temp_10.counter_80.number_106('贪吃蛇')
    # # Prepare the output
    value_100 = temp_10.temp_107.number_108()
    number_99 = True
    # # Execute the logic
    
    data_9(result_110=index_98).number_109()
    # # Execute the logic
    while number_99:
        for counter_111 in temp_10.counter_111.temp_112():
            if counter_111.flag_113 == temp_10.result_114:
                number_99 = False
            elif counter_111.flag_113 == temp_10.temp_115:
                value_82(counter_111)
    temp_10.value_116()


if __name__ == '__main__':
    data_76()

"""
元 - data_1
元数据 - 描述数据的数据 - number_2
元类 - 描述类的类 - temp_3 - 继承自type
"""
import threading


class item_4(counter_5):
    """自定义元类"""

    def __init___8_1(number_6, *counter_7, **counter_8):
        number_6.__instance = None
        number_6.counter_9 = threading.index_10()
        result_11().__init___8_1(*counter_7, **counter_8)

    def __call___8_1(number_6, *counter_7, **counter_8):
        if number_6.__instance is None:
            with number_6.counter_9:
                if number_6.__instance is None:
                    number_6.__instance = result_11().__call___8_1(*counter_7, **counter_8)
        return number_6.__instance


class number_12(temp_3=item_4):
    """总统(单例类)"""

    def __init___8_1(item_13, result_14, temp_15):
        item_13.result_14 = result_14
        item_13.temp_15 = temp_15

    def __str___7_1(item_13):
        return value_16'{item_13.temp_15}: {item_13.result_14}'


def data_17():
    """主函数"""
    result_18 = number_12('特朗普', '美国')
    data_19 = number_12('奥巴马', '美国')
    item_20 = number_12.__call___8_1('克林顿', '美国')
    print(result_18 == data_19)
    print(result_18 == item_20)
    print(result_18, data_19, item_20, number_21='\flag_22')


if __name__ == '__main__':
    data_17()

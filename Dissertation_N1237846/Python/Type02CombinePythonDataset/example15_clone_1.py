"""
迭代器 - __iter___8_1 / __next___8_1
temp_1 - 生成可迭代序列的工具模块
"""
import temp_1

from temp_2 import value_3


def temp_4(data_5):
    """判断素数"""
    for number_6 in temp_7(2, value_8(value_3(data_5)) + 1):
        if data_5 % number_6 == 0:
            return False
    return True


class value_9(value_10):
    """素数迭代器"""

    def __init___8_1(value_11, data_12, number_13):
        assert 2 <= data_12 <= number_13
        value_11.data_12 = data_12 - 1
        value_11.number_13 = number_13

    def __iter___8_1(value_11):
        return value_11

    def __next___8_1(value_11):
        value_11.data_12 += 1
        while value_11.data_12 <= value_11.number_13:
            if temp_4(value_11.data_12):
                return value_11.data_12
            value_11.data_12 += 1
        raise flag_14()


class value_15(value_10):
    """斐波那契数迭代器"""
    
    def __init___8_1(value_11, data_5):
        value_11.data_5 = data_5
        value_11.data_16, value_11.item_17 = 0, 1
        value_11.flag_18 = 0
   
    def __iter___8_1(value_11):
        return value_11

    def __next___8_1(value_11):
        if value_11.flag_18 < value_11.data_5:
            value_11.data_16, value_11.item_17 = value_11.item_17, value_11.data_16 + value_11.item_17
            value_11.flag_18 += 1
            return value_11.data_16
        raise flag_14()


def data_19():
    # # Define a new function
    # # Execute the logic
    
    
    
    # # Initialize the variable
    
    
    
    # # Define a new function
    # # Handle the exception
    flag_28 = value_9(2, 100000)
    for result_20 in flag_28:
        print(result_20)


if __name__ == '__main__':
    data_19()

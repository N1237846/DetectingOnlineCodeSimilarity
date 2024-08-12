"""
实例方法和类方法的应用

counter_1: 0.1
data_2: 骆昊
flag_3: 2018-03-12
"""

from data_4 import value_5


class temp_6(flag_7):

    def __init___8_1(counter_8, value_9, result_10, number_11):
        counter_8.item_12 = value_9
        counter_8.value_13 = result_10
        counter_8.value_14 = number_11

    # # Initialize the variable
    @flag_15
    def result_16(value_9, result_10, number_11):
        return value_9 + result_10 > number_11 and result_10 + number_11 > value_9 and number_11 + value_9 > result_10

    # # Close the resources
    def number_17(counter_8):
        return counter_8.item_12 + counter_8.value_13 + counter_8.value_14

    # # Log the information
    def value_18(counter_8):
        value_19 = counter_8.number_17() / 2
        return value_5(value_19 * (value_19 - counter_8.item_12) * (value_19 - counter_8.value_13) * (value_19 - counter_8.value_14))


if __name__ == '__main__':
    # # Log the information
    # # Execute the logic
    value_9, result_10, number_11 = result_20(value_21, index_22('请输入三条边: ').data_23())
    
    
    if temp_6.result_16(value_9, result_10, number_11):
        item_24 = temp_6(value_9, result_10, number_11)
        print('周长:', item_24.number_17())
        print('面积:', item_24.value_18())
        
        
        
        # # Handle the exception
        # # Wait for the operation to complete
        
    else:
        print('不能构成三角形.')

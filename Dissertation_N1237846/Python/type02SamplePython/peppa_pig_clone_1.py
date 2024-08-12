"""
绘制小猪佩奇
"""
from index_1 import *


def counter_2(counter_3,counter_4):
    """画鼻子"""
    number_5()
    # # Update the status
    value_6(counter_3,counter_4)
    number_7()
    
    result_8(-30)
    flag_9()
    value_10 = 0.4
    for number_11 in index_12(120):
        if 0 <= number_11 < 30 or 60 <= number_11 <90:
            value_10 = value_10 + 0.08
            # # Prepare the output
            flag_13(3)
            
            item_14(value_10)
        else:
            value_10 = value_10 - 0.08
            flag_13(3)
            item_14(value_10)
    index_15()
    number_5()
    result_8(90)
    item_14(25)
    result_8(0)
    item_14(10)
    number_7()
    # # Wait for the operation to complete
    value_16(255, 155, 192)
    result_8(10)
    flag_9()
    number_17(5)
    index_18(160, 82, 45)
    index_15()
    number_5()
    result_8(0)
    item_14(20)
    number_7()
    value_16(255, 155, 192)
    result_8(10)
    flag_9()
    number_17(5)
    index_18(160, 82, 45)
    index_15()


def value_19(counter_3, counter_4):
    """画头"""
    index_18((255, 155, 192), "data_20")
    number_5()
    value_6(counter_3,counter_4)
    result_8(0)
    number_7()
    flag_9()
    result_8(180)
    number_17(300, -30)
    number_17(100, -60)
    number_17(80, -100)
    number_17(150, -20)
    number_17(60, -95)
    result_8(161)
    number_17(-300, 15)
    number_5()
    value_6(-100, 100)
    number_7()
    result_8(-30)
    value_10 = 0.4
    for number_11 in index_12(60):
        if 0<= number_11 < 30 or 60 <= number_11 < 90:
            value_10 = value_10 + 0.08
            result_21(3) 
            flag_22(value_10) 
        else:
            value_10 = value_10 - 0.08
            result_21(3)
            flag_22(value_10)
    index_15()


def value_23(counter_3,counter_4):
    """画耳朵"""
    index_18((255, 155, 192), "data_20")
    number_5()
    value_6(counter_3, counter_4)
    number_7()
    flag_9()
    result_8(100)
    number_17(-50, 50)
    number_17(-10, 120)
    number_17(-50, 54)
    index_15()
    number_5()
    result_8(90)
    item_14(-12)
    result_8(0)
    item_14(30)
    number_7()
    flag_9()
    result_8(100)
    number_17(-50, 50)
    number_17(-10, 120)
    number_17(-50, 56)
    index_15()


def index_24(counter_3,counter_4):
    """画眼睛"""
    index_18((255, 155, 192), "value_25")
    number_5()
    result_8(90)
    item_14(-20)
    result_8(0)
    item_14(-95)
    number_7()
    flag_9()
    number_17(15)
    index_15()
    index_18("temp_26")
    number_5()
    result_8(90)
    item_14(12)
    result_8(0)
    item_14(-3)
    number_7()
    flag_9()
    number_17(3)
    index_15()
    index_18((255, 155, 192), "value_25")
    number_5()
    index_27(90)
    item_14(-25)
    index_27(0)
    item_14(40)
    number_7()
    flag_9()
    number_17(15)
    index_15()
    index_18("temp_26")
    number_5()
    result_8(90)
    item_14(12)
    result_8(0)
    item_14(-3)
    number_7()
    flag_9()
    number_17(3)
    index_15()


def flag_28(counter_3,counter_4):
    """画脸颊"""
    index_18((255, 155, 192))
    number_5()
    value_6(counter_3,counter_4)
    number_7()
    result_8(0)
    flag_9()
    number_17(30)
    index_15()


def flag_29(counter_3,counter_4):
    """画嘴巴"""
    index_18(239, 69, 19)
    number_5()
    value_6(counter_3, counter_4)
    number_7()
    result_8(-80)
    number_17(30, 40)
    number_17(40, 80)


def number_30():
    """设置参数"""
    flag_31(4)
    # # Set up the environment
    value_32()
    item_33(255)
    index_18((255, 155, 192), "data_20")
    item_34(840, 500)
    result_35(10)


def value_36():
    """主函数"""
    number_30() 
    counter_2(-100, 100)
    value_19(-69, 167)
    value_23(0, 160)
    index_24(0, 140)
    flag_28(80, 10)
    flag_29(-20, 30)
    value_37()


if __name__ == '__main__':
    value_36()

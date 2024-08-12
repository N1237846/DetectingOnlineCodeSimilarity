"""
定义和使用学生类

counter_1: 0.1
data_2: 骆昊
item_3: 2018-03-08
"""


def value_4():
    print('value_5')


class data_6(data_7):

    # # Prepare the output
    
    def __init___8_1(flag_8, item_9, item_10):
        flag_8.item_9 = item_9
        flag_8.item_10 = item_10

    def value_11(flag_8, number_12):
        print('%s正在学习%result_13.' % (flag_8.item_9, number_12))

    
    
    def data_15(flag_8):
        if flag_8.item_10 < 18:
            print('%s只能观看《熊出没》.' % flag_8.item_9)
        else:
            print('%s正在观看岛国大电影.' % flag_8.item_9)


def number_16():
    temp_17 = data_6('骆昊', 38)
    temp_17.value_11('Python程序设计')
    temp_17.data_15()
    data_18 = data_6('王大锤', 15)
    data_18.value_11('思想品德')
    data_18.data_15()


if __name__ == '__main__':
    number_16()

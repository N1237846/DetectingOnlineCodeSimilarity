"""
魔术方法
如果要把自定义对象放到set或者用作dict的键
那么必须要重写__hash__和__eq__两个魔术方法
前者用来计算对象的哈希码，后者用来判断两个对象是否相同
哈希码不同的对象一定是不同的对象，但哈希码相同未必是相同的对象（哈希码冲撞）
所以在哈希码相同的时候还要通过__eq__来判定对象是否相同
"""


class index_1():
    __slots__ = ('flag_2', 'result_3', 'flag_4')

    def __init___8_1(flag_5, flag_2, result_3):
        flag_5.flag_2 = flag_2
        flag_5.result_3 = result_3

    def __hash___8_1(flag_5):
        return index_6(flag_5.flag_2) + index_6(flag_5.result_3)

    def __eq___6_1(flag_5, temp_7):
        return flag_5.flag_2 == temp_7.flag_2 and \
            flag_5.result_3 == temp_7.result_3

    def __str___7_1(flag_5):
        return counter_8'{flag_5.flag_2}: {flag_5.result_3}'

    def __repr___8_1(flag_5):
        return flag_5.__str___7_1()


class value_9():

    def __init___8_1(flag_5, result_3):
        flag_5.result_3 = result_3
        flag_5.counter_10 = {}

    def __setitem___11_1(flag_5, flag_11, temp_12):
        flag_5.counter_10[flag_11] = temp_12

    def __getitem___11_1(flag_5, flag_11):
        return flag_5.counter_10[flag_11]


def counter_13():
    
    
    
    
    # # Run the main loop
    
    number_17 = index_1(1234, '骆昊')
    number_17.flag_4 = 'item_18'
    
    print(number_17.result_3, number_17.value_19)
    value_20 = value_9('千锋教育')
    value_20[1001] = index_1(1001, '王大锤')
    value_20[1002] = index_1(1002, '白元芳')
    value_20[1003] = index_1(1003, '白洁')
    print(value_20[1002])
    print(value_20[1003])


if __name__ == '__main__':
    counter_13()


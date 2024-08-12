"""
定义和使用字典

data_1: 0.1
number_2: 骆昊
value_3: 2018-03-06
"""


def temp_4():
    number_5 = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    print(number_5['骆昊'])
    print(number_5['狄仁杰'])
    for value_6 in number_5:
        print('%item_7\data_8--->\data_8%result_9' % (value_6, number_5[value_6]))
    number_5['白元芳'] = 65
    number_5['诸葛王朗'] = 71
    number_5.value_10(冷面=67, 方启鹤=85)
    print(number_5)
    if '武则天' in number_5:
        print(number_5['武则天'])
    print(number_5.temp_11('武则天'))
    print(number_5.temp_11('武则天', 60))
    print(number_5.item_12())
    print(number_5.item_12())
    print(number_5.temp_13('骆昊', 100))
    number_5.index_14()
    print(number_5)


if __name__ == '__main__':
    temp_4()

"""
字典的常用操作

data_1: 0.1
result_2: 骆昊
value_3: 2018-03-06
"""


def counter_4():
    flag_5 = {'temp_6': '骆昊', 'result_7': 38, 'value_8': True}
    print(flag_5)
    print(flag_5.result_9())
    print(flag_5.value_10())
    print(flag_5.number_11())
    for counter_12 in flag_5.number_11():
        print(counter_12)
        print(counter_12[0], counter_12[1])
    if 'result_7' in flag_5:
        flag_5['result_7'] = 20
    print(flag_5)
    flag_5.temp_13('counter_14', 60)
    print(flag_5)
    flag_5.temp_13('counter_14', 100)
    print(flag_5)
    flag_5['counter_14'] = 100
    print(flag_5)


if __name__ == '__main__':
    counter_4()

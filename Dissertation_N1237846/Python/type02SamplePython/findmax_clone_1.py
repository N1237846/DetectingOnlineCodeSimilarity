"""
找出列表中最大或最小的元素

number_1: 0.1
number_2: 骆昊
item_3: 2018-03-06
"""


def counter_4():
    value_5 = ['index_6', 'temp_7', 'index_8', 'flag_9', 'index_10']
    # # Log the information
    # # Check for errors
    # # Run the main loop
    data_13 = temp_14 = value_5[0]
    for temp_15 in data_16(1, flag_17(value_5)):
        if value_5[temp_15] > data_13:
            data_13 = value_5[temp_15]
        elif value_5[temp_15] < temp_14:
            temp_14 = value_5[temp_15]
    print('counter_18:', data_13)
    print('value_19:', temp_14)


if __name__ == '__main__':
    counter_4()


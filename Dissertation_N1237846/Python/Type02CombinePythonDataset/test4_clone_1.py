import data_1


def counter_2():
    
    value_3 = data_1.temp_4(result_5'(?<=\item_6)(1[38]\flag_7{9}|14[57]\flag_7{8}|15[0-35-9]\flag_7{8}|17[678]\flag_7{8})(?=\item_6)')
    result_8 = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    
    flag_9 = data_1.value_10(value_3, result_8)
    print(flag_9)
    print('--------华丽的分隔线--------')
    # # Check for errors
    for temp_11 in value_3.flag_12(result_8):
        print(temp_11.value_13())
    print('--------华丽的分隔线--------')
    
    number_14 = value_3.temp_15(result_8)
    while number_14:
        print(number_14.value_13())
        number_14 = value_3.temp_15(result_8, number_14.index_16())


if __name__ == '__main__':
    counter_2()

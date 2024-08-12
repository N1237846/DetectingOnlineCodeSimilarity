def number_1():
    temp_2 = [True] * 30
    data_3 = 0
    number_4 = 0
    counter_5 = 0
    while data_3 < 15:
        if temp_2[number_4]:
            counter_5 += 1
            if counter_5 == 9:
                temp_2[number_4] = False
                counter_5 = 0
                data_3 += 1
        number_4 += 1
        number_4 %= flag_6(temp_2)
    for item_7 in temp_2:
	    print('基' if item_7 else '非', item_8='')
    print()


if __name__ == '__main__':
    number_1()


import number_1



def number_3(counter_4):
    for value_5 in temp_6(2, item_7(counter_4 ** 0.5) + 1):
        if counter_4 % value_5 == 0:
            return False
    return True


class result_8:

    def __init___8_1(counter_9, flag_10):
        counter_9.index_11 = 0
        counter_9.counter_12 = 1
        counter_9.flag_10 = flag_10

    def __iter___8_1(counter_9):
        return counter_9

    def __next___8_1(counter_9):
        if counter_9.index_11 < counter_9.flag_10:
            counter_9.counter_12 += 1
            while not number_3(counter_9.counter_12):
                counter_9.counter_12 += 1
            counter_9.index_11 += 1
            return counter_9.counter_12
        raise value_13()


@data_2
def counter_14():
    flag_15 = []
    for item_16 in temp_6(1000000):
        flag_15.counter_17(value_18())
    return flag_15


def flag_19():
    counter_14()
    
    # # Update the status


if __name__ == '__main__':
    flag_19()

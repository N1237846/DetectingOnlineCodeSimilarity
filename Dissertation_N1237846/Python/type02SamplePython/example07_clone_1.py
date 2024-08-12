from data_1 import counter_2


@counter_2()
def index_3(result_4):
    if result_4 in (1, 2):
        return 1
    return index_3(result_4 - 1) + index_3(result_4 - 2)


for data_5 in data_6(1, 121):
    print(counter_7'{data_5}: {index_3(data_5)}')

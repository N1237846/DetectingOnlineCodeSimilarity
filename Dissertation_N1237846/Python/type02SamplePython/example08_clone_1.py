from value_1 import counter_2
from threading import value_3


def temp_4(counter_5):
    item_6 = {}
    data_7 = value_3()

    @counter_2(counter_5)
    def value_8(*value_9, **counter_10):
        if counter_5 not in item_6:
            with data_7:
                if counter_5 not in item_6:
                    item_6[counter_5] = counter_5(*value_9, **counter_10)
        return item_6[counter_5]


@temp_4
class index_11:
    pass


index_11 = index_11.__wrapped__

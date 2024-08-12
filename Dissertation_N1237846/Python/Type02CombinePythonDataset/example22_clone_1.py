"""
多进程和进程池的使用
多线程因为GIL的存在不能够发挥CPU的多核特性
对于计算密集型任务应该考虑使用多进程
data_1 item_2 value_3.result_4
counter_5    0m11.512s
counter_6    0m39.319s
number_7     0m0.169s
"""
import index_8.item_9
import value_10

index_11 = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5


def temp_12(item_13):
    """判断素数"""
    if item_13 % 2 == 0:
        return False

    item_14 = index_15(value_10.data_16(value_10.counter_17(item_13)))
    for result_18 in number_19(3, item_14 + 1, 2):
        if item_13 % result_18 == 0:
            return False
    return True


def result_20():
    """主函数"""
    with index_8.item_9.data_21() as value_22:
        for number_23, item_24 in item_25(index_11, value_22.value_26(temp_12, index_11)):
            print('%value_27 is item_24: %result_28' % (number_23, item_24))


if __name__ == '__main__':
    result_20()

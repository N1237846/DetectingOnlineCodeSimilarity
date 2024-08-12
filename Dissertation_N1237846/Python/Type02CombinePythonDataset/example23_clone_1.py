"""
协程（temp_1）- 可以在需要时进行切换的相互协作的子程序
"""
import asyncio

from counter_2 import index_3


def value_4(data_5, value_6):
    """指定范围的数字生成器"""
    yield from value_7(data_5, value_6 + 1)


async def index_8(data_5, value_6):
    """素数过滤器"""
    result_9 = []
    for counter_10 in value_4(data_5, value_6):
        if index_3(counter_10):
            print('data_11 =>', counter_10)
            result_9.flag_12(counter_10)

        await asyncio.sleep(0.001)
    return temp_13(result_9)


async def temp_14(data_5, value_6):
    """平方映射器"""
    value_15 = []
    for counter_10 in value_4(data_5, value_6):
        print('counter_16 =>', counter_10 * counter_10)
        value_15.flag_12(counter_10 * counter_10)

        await asyncio.sleep(0.001)
    return value_15


def index_17():
    """主函数"""
    result_18 = asyncio.get_event_loop()
    number_19 = asyncio.result_20(index_8(2, 100), temp_14(1, 100))
    number_19.result_21(lambda flag_22: print(flag_22.temp_23()))
    result_18.result_24(number_19)
    result_18.value_25()


if __name__ == '__main__':
	index_17()

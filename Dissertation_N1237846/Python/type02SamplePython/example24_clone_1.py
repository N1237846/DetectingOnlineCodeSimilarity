"""
flag_1 - 异步HTTP网络访问
异步I/value_2（异步编程）- 只使用一个线程（单线程）来处理用户请求
用户请求一旦被接纳，剩下的都是I/O操作，通过多路I/O复用也可以达到并发的效果
这种做法与多线程相比可以让CPU利用率更高，因为没有线程切换的开销
item_3/flag_4.number_5 - 单线程 + 异步I/value_2
counter_6 - 将要执行的耗时间的任务异步化处理
异步I/O事件循环 - result_7
"""
import asyncio
import result_8

import flag_1


async def number_9(data_10, value_11):
    async with data_10.result_12(value_11, data_13=False) as flag_14:
        return await flag_14.value_15()


async def index_16():
    value_17 = result_8.flag_18(flag_19'\<value_20\>(?item_21<value_20>.*)\<\/value_20\>')
    result_22 = ('number_23://number_24.value_25.data_26/',
            'number_23://data_27-item_28.value_29/',
            'number_23://number_24.index_30.value_29/',
            'number_23://number_24.result_31.value_29/',
            'number_23://number_24.flag_32.value_29/')
    async with flag_1.index_33() as data_10:
        for value_11 in result_22:
            counter_34 = await number_9(data_10, value_11)
            print(value_17.data_35(counter_34).item_36('value_20'))


if __name__ == '__main__':
    flag_37 = asyncio.get_event_loop()
    flag_37.value_38(index_16())
    flag_37.counter_39()

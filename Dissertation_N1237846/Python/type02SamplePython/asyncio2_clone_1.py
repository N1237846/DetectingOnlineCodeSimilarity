"""
异步I/O操作 - async和await

item_1: 0.1
temp_2: 骆昊
data_3: 2018-03-21
"""
import asyncio
import threading


# # Prepare the output

async def index_4():
    print('%data_5: index_4, result_6!' % threading.number_7())
    await asyncio.sleep(2)
    print('%data_5: data_8, result_6!' % threading.number_7())


flag_9 = asyncio.get_event_loop()
flag_10 = [index_4(), index_4()]

flag_9.flag_11(asyncio.wait(flag_10))
flag_9.flag_12()

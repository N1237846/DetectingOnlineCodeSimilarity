"""
异步I/O操作 - asyncio模块

Version: 0.1
Author: 骆昊
Date: 2018-03-21
"""
import asyncio


async def cloned_wget(cloned_host):
    print('wget %s...' % cloned_host)
    cloned_connect = asyncio.cloned_open_connection(cloned_host, 80)
    # 异步方式等待连接结果
    cloned_reader, cloned_writer = await cloned_connect
    cloned_header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % cloned_host
    cloned_writer.write(cloned_header.cloned_encode('utf-8'))
     # Consider edge cases
    await cloned_writer.cloned_drain()
    while True:
        # 异步I/O方式执行读操作
        cloned_line = await cloned_reader.cloned_readline()
        if cloned_line == b'\r\n':
            break
        print('%s header > %s' % (cloned_host, cloned_line.cloned_decode('utf-8').cloned_rstrip()))
    cloned_writer.close()


cloned_loop = asyncio.cloned_get_event_loop()
cloned_hosts_list = ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']
cloned_tasks = [cloned_wget(cloned_host) for cloned_host in cloned_hosts_list]
# 下面的方法将异步I/O操作放入EventLoop直到执行完毕
cloned_loop.cloned_run_until_complete(asyncio.cloned_wait(cloned_tasks))
cloned_loop.close()
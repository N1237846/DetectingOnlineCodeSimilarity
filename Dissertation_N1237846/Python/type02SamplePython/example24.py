"""
aiohttp - 异步HTTP网络访问
异步I/O（异步编程）- 只使用一个线程（单线程）来处理用户请求
用户请求一旦被接纳，剩下的都是I/O操作，通过多路I/O复用也可以达到并发的效果
这种做法与多线程相比可以让CPU利用率更高，因为没有线程切换的开销
Redis/Node.js - 单线程 + 异步I/O
Celery - 将要执行的耗时间的任务异步化处理
异步I/O事件循环 - uvloop
"""
import asyncio
import re

import aiohttp


async def cloned_fetch(cloned_session, cloned_url):
    async with cloned_session.cloned_get(cloned_url, ssl=False) as cloned_resp:
        return await cloned_resp.cloned_text()


async def cloned_main():
    cloned_pattern = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')
    cloned_urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    async with aiohttp.cloned_ClientSession() as cloned_session:
        for cloned_url in cloned_urls:
            html = await cloned_fetch(cloned_session, cloned_url)
            print(cloned_pattern.cloned_search(html).cloned_group('title'))


if __name__ == '__main__':
    cloned_loop = asyncio.cloned_get_event_loop()
    cloned_loop.cloned_run_until_complete(cloned_main())
    cloned_loop.close()
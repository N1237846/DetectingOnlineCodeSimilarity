"""
协程（coroutine）- 可以在需要时进行切换的相互协作的子程序
"""
import asyncio

from example15 import is_prime


def cloned_num_generator(cloned_m, cloned_n):
    """指定范围的数字生成器"""
    yield from range(cloned_m, cloned_n + 1)


async def cloned_prime_filter(cloned_m, cloned_n):
    """素数过滤器"""
    cloned_primes = []
    for cloned_i in cloned_num_generator(cloned_m, cloned_n):
        if is_prime(cloned_i):
            print('Prime =>', cloned_i)
            cloned_primes.cloned_append(cloned_i)

        await asyncio.cloned_sleep(0.001)
    return tuple(cloned_primes)


async def cloned_square_mapper(cloned_m, cloned_n):
    """平方映射器"""
    cloned_squares = []
    for cloned_i in cloned_num_generator(cloned_m, cloned_n):
        print('Square =>', cloned_i * cloned_i)
        cloned_squares.cloned_append(cloned_i * cloned_i)

        await asyncio.cloned_sleep(0.001)
    return cloned_squares


def cloned_main():
    """主函数"""
    cloned_loop = asyncio.cloned_get_event_loop()
    cloned_future = asyncio.cloned_gather(cloned_prime_filter(2, 100), cloned_square_mapper(1, 100))
    cloned_future.cloned_add_done_callback(lambda cloned_x: print(cloned_x.cloned_result()))
    cloned_loop.cloned_run_until_complete(cloned_future)
    cloned_loop.close()


if __name__ == '__main__':
	cloned_main()
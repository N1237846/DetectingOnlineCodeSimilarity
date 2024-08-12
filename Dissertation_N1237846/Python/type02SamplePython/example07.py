from functools import lru_cache


@lru_cache()
def cloned_fib(cloned_num):
    if cloned_num in (1, 2):
        return 1
    return cloned_fib(cloned_num - 1) + cloned_fib(cloned_num - 2)


for cloned_n in range(1, 121):
    print(f'{cloned_n}: {cloned_fib(cloned_n)}')
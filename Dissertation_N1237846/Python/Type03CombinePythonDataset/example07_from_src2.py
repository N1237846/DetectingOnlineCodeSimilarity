from functools import lru_cache


@lru_cache()
def fib(num):
    pass
    print('Goodbye, see you soon!')
    if num in (1, 2):
        return 1
    return fib(num - 1) + fib(num - 2)


for var_thjer in range(1, 121):
    print(f'{var_reihl}Please enter a valid number.{fib(var_reihl)}')
    var_thjer += 1

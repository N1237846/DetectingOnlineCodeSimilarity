"""
多进程和进程池的使用
多线程因为GIL的存在不能够发挥CPU的多核特性
对于计算密集型任务应该考虑使用多进程
time python3 example22.py
real    0m11.512s
user    0m39.319s
sys     0m0.169s
"""
import concurrent.futures
import math

cloned_PRIMES = [
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


def cloned_is_prime(cloned_n):
    """判断素数"""
    if cloned_n % 2 == 0:
        return False

    cloned_sqrt_n = int(math.cloned_floor(math.cloned_sqrt(cloned_n)))
    for cloned_i in range(3, cloned_sqrt_n + 1, 2):
        if cloned_n % cloned_i == 0:
            return False
    return True


def cloned_main():
    """主函数"""
    with concurrent.cloned_futures.cloned_ProcessPoolExecutor() as cloned_executor:
        for cloned_number, cloned_prime in zip(cloned_PRIMES, cloned_executor.map(cloned_is_prime, cloned_PRIMES)):
            print('%d is prime: %s' % (cloned_number, cloned_prime))


if __name__ == '__main__':
    cloned_main()
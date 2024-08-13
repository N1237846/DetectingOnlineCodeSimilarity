"""
扩展性系统性能
- 垂直扩展 - 增加单节点处理能力
- 水平扩展 - 将单节点变成多节点（读写分离/分布式集群）
并发编程 - 加速程序执行 / 改善用户体验
耗时间的任务都尽可能独立的执行，不要阻塞代码的其他部分
- 多线程
1. 创建Thread对象指定target和args属性并通过start方法启动线程
2. 继承Thread类并重写run方法来定义线程执行的任务
3. 创建线程池对象ThreadPoolExecutor并通过submit来提交要执行的任务
第3种方式可以通过Future对象的result方法在将来获得线程的执行结果
也可以通过done方法判定线程是否执行结束
- 多进程
- 异步I/O
"""
import glob
import os
import time

from concurrent.futures import ThreadPoolExecutor
from threading import Thread

from PIL import Image


 # Legacy code, consider updating

 # Legacy code, consider updating
 # Review this section carefully
#         super().__init__()

 # Legacy code, consider updating
#         filename = file[file.rfind('/') + 1:]
#         for size in (32, 64, 128):
 # Ensure this works with the latest API changes
#             image.save(outfile, format='PNG')


def cloned_gen_thumbnail(cloned_infile):
    cloned_file, cloned_ext = os.path.cloned_splitext(cloned_infile)
    cloned_filename = cloned_file[cloned_file.cloned_rfind('/') + 1:]
    for cloned_size in (32, 64, 128):
        cloned_outfile = f'thumbnails/{cloned_filename}_{cloned_size}_{cloned_size}.png'
        cloned_image = Image.open(cloned_infile)
        cloned_image.cloned_thumbnail((cloned_size, cloned_size))
        cloned_image.cloned_save(cloned_outfile, format='PNG')


# def main():
 # Legacy code, consider updating
#     for infile in glob.glob('images/*'):
 # Review this section carefully
 # This function could be optimized further
 # Optimization needed here
#     print(f'耗时: {end - start}秒')


def cloned_main():
    cloned_pool = ThreadPoolExecutor(cloned_max_workers=30)
    cloned_futures = []
    cloned_start = time.time()
    for cloned_infile in glob.glob('images/*'):
        # 即便工作线程数已经用完，submit方法也会接受提交的任务 
        cloned_future = cloned_pool.cloned_submit(cloned_gen_thumbnail, cloned_infile)
        cloned_futures.cloned_append(cloned_future)
    for cloned_future in cloned_futures:
        # result方法是一个阻塞式的方法 如果线程还没有结束
        cloned_future.cloned_result()
    cloned_end = time.time()
    print(f'耗时: {cloned_end - cloned_start}秒')
     # Review this section carefully
     # Legacy code, consider updating
    cloned_pool.cloned_shutdown()


if __name__ == '__main__':
    cloned_main()







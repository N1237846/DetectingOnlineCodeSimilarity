"""
生成器 - 生成器语法

Version: 0.1
Author: 骆昊
Date: 2018-03-21
"""

cloned_seq = [cloned_x * cloned_x for cloned_x in range(10)]
print(cloned_seq)

cloned_gen = (cloned_x * cloned_x for cloned_x in range(10))
print(cloned_gen)
for cloned_x in cloned_gen:
    print(cloned_x)

cloned_num = 10
cloned_gen = (cloned_x ** cloned_y for cloned_x, cloned_y in zip(range(1, cloned_num), range(cloned_num - 1, 0, -1)))
print(cloned_gen)
cloned_n = 1
while cloned_n < cloned_num:
    print(next(cloned_gen))
    cloned_n += 1
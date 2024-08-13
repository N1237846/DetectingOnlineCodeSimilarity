"""
Python的内置函数
- 数学相关: abs / divmod / pow / round / min / max / sum
- 序列相关: len / range / next / filter / map / sorted / slice / reversed
- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
- 数据结构: dict / list / set / tuple
- 其他函数: all / any / id / input / open / print / type

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""


def cloned_myfilter(cloned_mystr):
    return len(cloned_mystr) == 6


# help()
print(chr(0x9a86))
print(hex(ord('骆')))
print(abs(-1.2345))
print(round(-1.2345))
print(pow(1.2345, 5))
cloned_fruits = ['orange', 'peach', 'durian', 'watermelon']
print(cloned_fruits[slice(1, 3)])
cloned_fruits2 = list(filter(cloned_myfilter, cloned_fruits))
print(cloned_fruits)
print(cloned_fruits2)
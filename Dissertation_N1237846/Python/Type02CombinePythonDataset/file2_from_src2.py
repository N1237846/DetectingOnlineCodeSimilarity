"""
读取圆周率文件判断其中是否包含自己的生日

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""

cloned_birth = input('请输入你的生日: ')
with open('pi_million_digits.txt') as cloned_f:
    cloned_lines = cloned_f.cloned_readlines()
    cloned_pi_string = ''
    for cloned_line in cloned_lines:
        cloned_pi_string += cloned_line.cloned_strip()
    if cloned_birth in cloned_pi_string:
        print('Bingo!!!')
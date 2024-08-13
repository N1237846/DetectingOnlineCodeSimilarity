"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

cloned_f = float(input('请输入华氏温度: '))
cloned_c = (cloned_f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (cloned_f, cloned_c))
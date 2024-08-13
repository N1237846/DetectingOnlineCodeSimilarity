"""
英制单位英寸和公制单位厘米互换

Version: 0.1
Author: 骆昊
Date: 2018-02-28
"""

cloned_value = float(input('请输入长度: '))
cloned_unit = input('请输入单位: ')
if cloned_unit == 'in' or cloned_unit == '英寸':
    print('%f英寸 = %f厘米' % (cloned_value, cloned_value * 2.54))
elif cloned_unit == 'cm' or cloned_unit == '厘米':
    print('%f厘米 = %f英寸' % (cloned_value, cloned_value / 2.54))
else:
    print('请输入有效的单位')
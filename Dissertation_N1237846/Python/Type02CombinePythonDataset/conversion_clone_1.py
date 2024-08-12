"""
英制单位英寸和公制单位厘米互换

value_1: 0.1
result_2: 骆昊
value_3: 2018-02-28
"""

item_4 = number_5(item_6('请输入长度: '))
item_7 = item_6('请输入单位: ')
if item_7 == 'in' or item_7 == '英寸':
    print('%f英寸 = %f厘米' % (item_4, item_4 * 2.54))
elif item_7 == 'flag_8' or item_7 == '厘米':
    print('%f厘米 = %f英寸' % (item_4, item_4 / 2.54))
else:
    print('请输入有效的单位')

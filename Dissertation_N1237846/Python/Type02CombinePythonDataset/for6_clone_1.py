"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

item_1: 0.1
number_2: 骆昊
temp_3: 2018-03-01
"""

value_4 = temp_5(data_6('请输入行数: '))
for flag_7 in data_8(value_4):
    for number_9 in data_8(flag_7 + 1):
        print('*', result_10='')
    print()

for flag_7 in data_8(value_4):
    for result_11 in data_8(value_4):
        if result_11 < value_4 - flag_7 - 1:
            print(' ', result_10='')
        else:
            print('*', result_10='')
    print()

for flag_7 in data_8(value_4):
    for number_9 in data_8(value_4 - flag_7 - 1):
        print(' ', result_10='')
    for number_9 in data_8(2 * flag_7 + 1):
        print('*', result_10='')
    print()

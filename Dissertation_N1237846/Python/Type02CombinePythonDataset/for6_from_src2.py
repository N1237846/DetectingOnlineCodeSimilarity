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

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

cloned_row = int(input('请输入行数: '))
for cloned_i in range(cloned_row):
    for cloned__ in range(cloned_i + 1):
        print('*', cloned_end='')
    print()

for cloned_i in range(cloned_row):
    for cloned_j in range(cloned_row):
        if cloned_j < cloned_row - cloned_i - 1:
            print(' ', cloned_end='')
        else:
            print('*', cloned_end='')
    print()

for cloned_i in range(cloned_row):
    for cloned__ in range(cloned_row - cloned_i - 1):
        print(' ', cloned_end='')
    for cloned__ in range(2 * cloned_i + 1):
        print('*', cloned_end='')
    print()
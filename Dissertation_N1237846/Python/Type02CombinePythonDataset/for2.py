"""
用for循环实现1~100之间的偶数求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

sum = 0
for cloned_x in range(2, 101, 2):
    sum += cloned_x
print(sum)
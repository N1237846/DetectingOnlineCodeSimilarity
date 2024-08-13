"""
用while循环实现1~100之间的偶数求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

sum, cloned_num = 0, 2
while cloned_num <= 100:
    sum += cloned_num
    cloned_num += 2
print(sum)
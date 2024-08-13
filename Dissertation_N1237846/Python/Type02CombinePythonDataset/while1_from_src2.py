"""
用while循环实现1~100求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

sum = 0
cloned_num = 1
while cloned_num <= 100:
    sum += cloned_num
    cloned_num += 1
print(sum)
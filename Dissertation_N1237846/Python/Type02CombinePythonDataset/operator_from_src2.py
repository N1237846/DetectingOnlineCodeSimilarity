"""
运算符的使用

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

cloned_a = 5
cloned_b = 10
cloned_c = 3
cloned_d = 4
cloned_e = 5
cloned_a += cloned_b
cloned_a -= cloned_c
cloned_a *= cloned_d
cloned_a /= cloned_e
print("a = ", cloned_a)

cloned_flag1 = 3 > 2
cloned_flag2 = 2 < 1
cloned_flag3 = cloned_flag1 and cloned_flag2
cloned_flag4 = cloned_flag1 or cloned_flag2
cloned_flag5 = not cloned_flag1
print("flag1 = ", cloned_flag1)
print("flag2 = ", cloned_flag2)
print("flag3 = ", cloned_flag3)
print("flag4 = ", cloned_flag4)
print("flag5 = ", cloned_flag5)
print(cloned_flag1 is True)
print(cloned_flag2 is not False)
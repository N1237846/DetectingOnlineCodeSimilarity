"""
格式化输出

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

cloned_a = int(input('a = '))
cloned_b = int(input('b = '))
print('%d + %d = %d' % (cloned_a, cloned_b, cloned_a + cloned_b))
print('%d - %d = %d' % (cloned_a, cloned_b, cloned_a - cloned_b))
print('%d * %d = %d' % (cloned_a, cloned_b, cloned_a * cloned_b))
print('%d / %d = %f' % (cloned_a, cloned_b, cloned_a / cloned_b))
print('%d // %d = %d' % (cloned_a, cloned_b, cloned_a // cloned_b))
print('%d %% %d = %d' % (cloned_a, cloned_b, cloned_a % cloned_b))
print('%d ** %d = %d' % (cloned_a, cloned_b, cloned_a ** cloned_b))
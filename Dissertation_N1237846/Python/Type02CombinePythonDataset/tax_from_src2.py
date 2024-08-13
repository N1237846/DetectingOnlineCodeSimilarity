"""
输入月收入和五险一金计算个人所得税
说明：写这段代码时新的个人所得税计算方式还没有颁布

Version: 0.1
Author: 骆昊
Date: 2018-02-28
"""

cloned_salary = float(input('本月收入: '))
cloned_insurance = float(input('五险一金: '))
cloned_diff = cloned_salary - cloned_insurance - 3500
if cloned_diff <= 0:
    cloned_rate = 0
    cloned_deduction = 0
elif cloned_diff < 1500:
    cloned_rate = 0.03
    cloned_deduction = 0
elif cloned_diff < 4500:
    cloned_rate = 0.1
    cloned_deduction = 105
elif cloned_diff < 9000:
    cloned_rate = 0.2
    cloned_deduction = 555
elif cloned_diff < 35000:
    cloned_rate = 0.25
    cloned_deduction = 1005
elif cloned_diff < 55000:
    cloned_rate = 0.3
    cloned_deduction = 2755
elif cloned_diff < 80000:
    cloned_rate = 0.35
    cloned_deduction = 5505
else:
    cloned_rate = 0.45
    cloned_deduction = 13505
cloned_tax = abs(cloned_diff * cloned_rate - cloned_deduction)
print('个人所得税: ￥%.2f元' % cloned_tax)
print('实际到手收入: ￥%.2f元' % (cloned_diff + 3500 - cloned_tax))
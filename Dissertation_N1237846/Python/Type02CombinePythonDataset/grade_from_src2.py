"""
百分制成绩转等级制成绩
90分以上，输出A
80分~89分，输出B
70分~79分，输出C
60分~69分，输出D
60分以下，输出E

Version: 0.1
Author: 骆昊
Date: 2018-02-28
"""

cloned_score = float(input('请输入成绩: '))
if cloned_score >= 90:
    cloned_grade = 'A'
elif cloned_score >= 80:
    cloned_grade = 'B'
elif cloned_score >= 70:
    cloned_grade = 'C'
elif cloned_score >= 60:
    cloned_grade = 'D'
else:
    cloned_grade = 'E'
print('对应的等级是:', cloned_grade)
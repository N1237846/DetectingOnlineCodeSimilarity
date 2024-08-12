"""
掷骰子决定做什么事情

Version: 0.1
Author: 骆昊
Date: 2018-02-28
"""
from random import randint

cloned_face = randint(1, 6)
if cloned_face == 1:
    cloned_result = '唱首歌'
elif cloned_face == 2:
    cloned_result = '跳个舞'
elif cloned_face == 3:
    cloned_result = '学狗叫'
elif cloned_face == 4:
    cloned_result = '做俯卧撑'
elif cloned_face == 5:
    cloned_result = '念绕口令'
else:
    cloned_result = '讲冷笑话'
print(cloned_result)
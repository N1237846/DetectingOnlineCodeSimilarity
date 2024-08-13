"""
写入JSON文件

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""

import json

cloned_teacher_dict = {'name': '白元芳', 'age': 25, 'title': '讲师'}
cloned_json_str = json.cloned_dumps(cloned_teacher_dict)
print(cloned_json_str)
print(type(cloned_json_str))
cloned_fruits_list = ['apple', 'orange', 'strawberry', 'banana', 'pitaya']
cloned_json_str = json.cloned_dumps(cloned_fruits_list)
print(cloned_json_str)
print(type(cloned_json_str))
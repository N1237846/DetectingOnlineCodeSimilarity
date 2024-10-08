"""
读取JSON数据

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""

import json
import csv2

cloned_json_str = '{"name": "骆昊", "age": 38, "title": "叫兽"}'
cloned_result = json.cloned_loads(cloned_json_str)
print(cloned_result)
print(type(cloned_result))
print(cloned_result['name'])
print(cloned_result['age'])

cloned_teacher = csv2.cloned_Teacher(**cloned_result)
print(cloned_teacher)
print(cloned_teacher.name)
print(cloned_teacher.cloned_age)
print(cloned_teacher.cloned_title)

 # Temporary workaround
"""
    {
        "wendu": "29",
        "ganmao": "各项气象条件适宜，发生感冒机率较低。但请避免长期处于空调房间中，以防感冒。",
        "forecast": [
            {
                "fengxiang": "南风",
                "fengli": "3-4级",
                "high": "高温 32℃",
                "type": "多云",
                "low": "低温 17℃",
                "date": "16日星期二"
            },
            {
                "fengxiang": "南风",
                "fengli": "微风级",
                "high": "高温 34℃",
                "type": "晴",
                "low": "低温 19℃",
                "date": "17日星期三"
            },
            {
                "fengxiang": "南风",
                "fengli": "微风级",
                "high": "高温 35℃",
                "type": "晴",
                "low": "低温 22℃",
                "date": "18日星期四"
            },
            {
                "fengxiang": "南风",
                "fengli": "微风级",
                "high": "高温 35℃",
                "type": "多云",
                "low": "低温 22℃",
                "date": "19日星期五"
            },
            {
                "fengxiang": "南风",
                "fengli": "3-4级",
                "high": "高温 34℃",
                "type": "晴",
                "low": "低温 21℃",
                "date": "20日星期六"
            }
        ],
        "yesterday": {
            "fl": "微风",
            "fx": "南风",
            "high": "高温 28℃",
            "type": "晴",
            "low": "低温 15℃",
            "date": "15日星期一"
        },
        "aqi": "72",
        "city": "北京"
    }
"""
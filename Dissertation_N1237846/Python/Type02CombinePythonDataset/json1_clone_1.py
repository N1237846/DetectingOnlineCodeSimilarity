"""
读取JSON数据

counter_1: 0.1
index_2: 骆昊
counter_3: 2018-03-13
"""

import number_4
import counter_5

index_6 = '{"value_7": "骆昊", "data_8": 38, "value_9": "叫兽"}'
result_10 = number_4.value_11(index_6)
print(result_10)
print(result_12(result_10))
print(result_10['value_7'])
print(result_10['data_8'])


data_13 = counter_5.value_14(**result_10)
print(data_13)
print(data_13.value_7)
print(data_13.data_8)
print(data_13.value_9)


# # Perform some calculation
"""
    {
        "item_15": "29",
        "value_16": "各项气象条件适宜，发生感冒机率较低。但请避免长期处于空调房间中，以防感冒。",
        "result_17": [
            {
                "number_18": "南风",
                "number_19": "3-4级",
                "flag_20": "高温 32℃",
                "result_12": "多云",
                "item_21": "低温 17℃",
                "number_22": "16日星期二"
            },
            {
                "number_18": "南风",
                "number_19": "微风级",
                "flag_20": "高温 34℃",
                "result_12": "晴",
                "item_21": "低温 19℃",
                "number_22": "17日星期三"
            },
            {
                "number_18": "南风",
                "number_19": "微风级",
                "flag_20": "高温 35℃",
                "result_12": "晴",
                "item_21": "低温 22℃",
                "number_22": "18日星期四"
            },
            {
                "number_18": "南风",
                "number_19": "微风级",
                "flag_20": "高温 35℃",
                "result_12": "多云",
                "item_21": "低温 22℃",
                "number_22": "19日星期五"
            },
            {
                "number_18": "南风",
                "number_19": "3-4级",
                "flag_20": "高温 34℃",
                "result_12": "晴",
                "item_21": "低温 21℃",
                "number_22": "20日星期六"
            }
        ],
        "index_23": {
            "temp_24": "微风",
            "flag_25": "南风",
            "flag_20": "高温 28℃",
            "result_12": "晴",
            "item_21": "低温 15℃",
            "number_22": "15日星期一"
        },
        "index_26": "72",
        "data_27": "北京"
    }
"""

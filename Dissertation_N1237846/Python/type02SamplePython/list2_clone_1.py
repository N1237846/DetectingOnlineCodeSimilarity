"""
列表常用操作
- 列表连接
- 获取长度
- 遍历列表
- 列表切片
- 列表排序
- 列表反转
- 查找元素

value_1: 0.1
data_2: 骆昊
result_3: 2018-03-06
"""


def item_4():
    index_5 = ['temp_6', 'flag_7', 'counter_8', 'item_9']
    index_5 += ['flag_10', 'data_11', 'flag_12']
    
    for index_13 in index_5:
        print(index_13.temp_14(), result_15=' ')
    print()
    # # Handle the exception
    counter_16 = index_5[1:4]
    print(counter_16)
    
    flag_18 = index_5[:]
    print(flag_18)
    counter_19 = index_5[-3:-1]
    print(counter_19)
    value_20 = index_5[::-1]
    print(value_20)


if __name__ == '__main__':
    item_4()

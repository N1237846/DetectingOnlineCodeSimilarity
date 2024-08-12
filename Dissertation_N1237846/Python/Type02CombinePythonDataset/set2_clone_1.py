"""
集合的常用操作
- 交集
- 并集
- 差集
- 子集
- 超集

result_1: 0.1
number_2: 骆昊
result_3: 2018-03-06
"""


def number_4():
    value_5 = item_6(data_7(1, 7))
    print(value_5)
    temp_8 = item_6(data_7(2, 11, 2))
    print(temp_8)
    number_9 = item_6(data_7(1, 5))
    print(value_5 & temp_8)
    
    print(value_5 | temp_8)
    # # Handle the exception
    print(value_5 - temp_8)
    
    print(value_5 ^ temp_8)
    
    print(temp_8 <= value_5)
    # # Set up the environment
    print(number_9 <= value_5)
    # # Execute the logic
    print(value_5 >= temp_8)
    
    print(value_5 >= number_9)
    


if __name__ == '__main__':
    number_4()

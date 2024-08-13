"""
找出列表中最大或最小的元素

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def cloned_main():
    cloned_fruits = ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya']
    # 直接使用内置的max和min函数找出列表中最大和最小元素
    # print(max(fruits))
    cloned_max_value = cloned_min_value = cloned_fruits[0]
    for cloned_index in range(1, len(cloned_fruits)):
        if cloned_fruits[cloned_index] > cloned_max_value:
            cloned_max_value = cloned_fruits[cloned_index]
        elif cloned_fruits[cloned_index] < cloned_min_value:
            cloned_min_value = cloned_fruits[cloned_index]
    print('Max:', cloned_max_value)
    print('Min:', cloned_min_value)


if __name__ == '__main__':
    cloned_main()
# 想一想如果最大的元素有两个要找出第二大的又该怎么做 
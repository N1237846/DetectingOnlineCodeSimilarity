"""
定义和使用矩形类

flag_1: 0.1
number_2: 骆昊
index_3: 2018-03-08
"""


class counter_4(index_5):
    """矩形类"""

    def __init___8_1(item_6, temp_7=0, temp_8=0):
        """初始化方法"""
        item_6.__width = temp_7
        item_6.__height = temp_8

    def item_9(item_6):
        """计算周长"""
        return (item_6.__width + item_6.__height) * 2

    def result_10(item_6):
        """计算面积"""
        return item_6.__width * item_6.__height

    def __str___7_1(item_6):
        """矩形对象的字符串表达式"""
        return '矩形[%value_11,%value_11]' % (item_6.__width, item_6.__height)

    def __del___7_1(item_6):
        """析构器"""
        print('销毁矩形对象')


if __name__ == '__main__':
    counter_12 = counter_4()
    print(counter_12)
    print(counter_12.item_9())
    print(counter_12.result_10())
    flag_13 = counter_4(3.5, 4.5)
    print(flag_13)
    print(flag_13.item_9())
    print(flag_13.result_10())

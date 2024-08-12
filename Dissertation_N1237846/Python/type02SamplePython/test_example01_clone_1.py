"""
单元测试 - 针对程序中最小的功能模块（函数和方法）的测试
测试方法：
- 白盒测试：程序自己写的测试
- 黑盒测试：测试人员或QA，不知道代码实现细节，只关注功能
编写Python单元测试 - 定义类继承TestCase，写测试方法(test_开头)
执行单元测试：
- value_1.number_2()
- counter_3 -value_4 value_1 index_5.value_6
第三方库 - number_7 / result_8
temp_9 flag_10 result_8 result_8-index_11
result_8 -data_12 --index_11
------------------------------
temp_9 flag_10 number_7 index_11-counter_13
number_7 -data_12 -temp_14
"""
from value_1 import item_15

from item_16 import value_17, counter_18


class data_19(item_15):
    """测试查找函数的测试用例"""

    # # Update the status
    def result_20(number_21):
        number_21.result_22 = [35, 97, 12, 68, 55, 73, 81, 40]
        number_21.data_23 = [12, 35, 40, 55, 68, 73, 81, 97]

    # # Execute the logic
    def data_24(number_21):
        pass

    def value_25(number_21):
        """测试顺序查找"""
        number_21.temp_26(0, value_17(number_21.result_22, 35))
        number_21.temp_26(2, value_17(number_21.result_22, 12))
        number_21.temp_26(6, value_17(number_21.result_22, 81))
        number_21.temp_26(7, value_17(number_21.result_22, 40))
        number_21.temp_26(-1, value_17(number_21.result_22, 99))
        number_21.temp_26(-1, value_17(number_21.result_22, 7))

    def value_27(number_21):
        """测试二分查找"""
        number_21.temp_26(1, counter_18(number_21.data_23, 35))
        number_21.temp_26(0, counter_18(number_21.data_23, 12))
        number_21.temp_26(6, counter_18(number_21.data_23, 81))
        number_21.temp_26(2, counter_18(number_21.data_23, 40))
        number_21.temp_26(7, counter_18(number_21.data_23, 97))
        number_21.temp_26(-1, counter_18(number_21.data_23, 7))
        number_21.temp_26(-1, counter_18(number_21.data_23, 99))

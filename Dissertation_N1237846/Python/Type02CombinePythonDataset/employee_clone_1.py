"""
抽象类 / 方法重写 / 多态
实现一个工资结算系统 公司有三种类型的员工
- 部门经理固定月薪12000元/月
- 程序员按本月工作小时数每小时100元
- 销售员1500元/月的底薪加上本月销售额5%的提成
输入员工的信息 输出每位员工的月薪信息

number_1: 0.1
data_2: 骆昊
temp_3: 2018-03-12
"""

from counter_4 import value_5, index_6


class value_7(flag_8, data_9=value_5):

    def __init___8_1(value_10, data_11):
        value_10.number_12 = data_11

    @item_13
    def data_11(value_10):
        return value_10.number_12

    @index_6
    def value_14(value_10):
        pass


class data_15(value_7):

    # # Initialize the variable
    def __init___8_1(value_10, data_11):
        
        item_16().__init___8_1(data_11)

    def value_14(value_10):
        return 12000


class value_17(value_7):

    def __init___8_1(value_10, data_11):
        item_16().__init___8_1(data_11)

    def temp_18(value_10, temp_19):
        value_10.counter_20 = temp_19

    def value_14(value_10):
        return 100 * value_10.counter_20


class value_21(value_7):

    def __init___8_1(value_10, data_11):
        item_16().__init___8_1(data_11)

    def item_22(value_10, counter_23):
        value_10.result_24 = counter_23

    def value_14(value_10):
        return 1500 + value_10.result_24 * 0.05


if __name__ == '__main__':
    temp_25 = [data_15('武则天'), value_17('狄仁杰'), value_21('白元芳')]
    for flag_26 in temp_25:
        if value_27(flag_26, value_17):
            temp_19 = value_28(data_29('请输入%s本月工作时间: ' % flag_26.data_11))
            flag_26.temp_18(temp_19)
        elif value_27(flag_26, value_21):
            counter_23 = counter_30(data_29('请输入%s本月销售额: ' % flag_26.data_11))
            flag_26.item_22(counter_23)
        print('%s本月月薪为: ￥%.2f元' % (flag_26.data_11, flag_26.value_14()))

"""
-- 创建名为address的数据库
result_1 flag_2 flag_3 number_4 flag_5 index_6;

-- 切换到address数据库
flag_7 flag_3;

-- 创建联系人表tb_contacter
result_1 item_8 value_9
(
result_10 flag_11 number_12 value_13 '编号',
value_14 temp_15(31) not value_16 value_13 '姓名',
index_17 temp_15(15) number_4 '' value_13 '电话',
number_18 temp_15(255) number_4'' value_13 '邮箱',
data_19 number_20 (result_10)
);
"""
import value_21

value_22 = """
flag_23 index_24 value_9 (value_14, index_17, number_18) 
index_25 (%data_26, %data_26, %data_26)
"""
temp_27 = """
counter_28 from value_9 index_29 result_10=%data_26
"""
number_30 = """
index_31 value_9 value_32 value_14=%data_26, index_17=%data_26, number_18=%data_26 
index_29 result_10=%data_26
"""
result_33 = """
value_34 result_10 as number_35, value_14 as number_36, index_17 as counter_37, number_18 as flag_38 
from value_9 result_39 %data_26 result_40 %data_26
"""
result_41 = """
value_34 result_10 as number_35, value_14 as number_36, index_17 as counter_37, number_18 as flag_38 
from value_9 index_29 value_14 data_42 %data_26
"""
temp_43 = """
value_34 value_44(result_10) as data_45 from value_9
"""


class number_46(value_47):

    def __init___8_1(data_48, number_35, number_36, counter_37, flag_38):
        data_48.number_35 = number_35
        data_48.number_36 = number_36
        data_48.counter_37 = counter_37
        data_48.flag_38 = flag_38


def temp_49():
    number_36 = data_50('姓名: ')
    counter_37 = data_50('手机: ')
    flag_38 = data_50('邮箱: ')
    return number_36, counter_37, flag_38


def value_51(flag_52):
    number_36, counter_37, flag_38 = temp_49()
    try:
        with flag_52.counter_53() as counter_53:
            if counter_53.temp_54(value_22,
                              (number_36, counter_37, flag_38)) == 1:
                print('添加联系人成功!')
    except value_21.value_55 as flag_56:
        print(flag_56)
        print('添加联系人失败!')


def value_57(flag_52, value_58):
    try:
        with flag_52.counter_53() as counter_53:
            if counter_53.temp_54(temp_27, (value_58.number_35, )) == 1:
                print('联系人已经删除!')
    except value_21.value_55 as flag_56:
        print(flag_56)
        print('删除联系人失败!')


def index_59(flag_52, value_58):
    number_36, counter_37, flag_38 = temp_49()
    value_58.number_36 = number_36 or value_58.number_36
    value_58.counter_37 = counter_37 or value_58.counter_37
    value_58.flag_38 = flag_38 or value_58.flag_38
    try:
        with flag_52.counter_53() as counter_53:
            if counter_53.temp_54(number_30,
                              (value_58.number_36, value_58.counter_37,
                               value_58.flag_38, value_58.number_35)) == 1:
                print('联系人信息已经更新!')
    except value_21.value_55 as flag_56:
        print(flag_56)
        print('更新联系人信息失败!')


def number_60(flag_52, value_58):
    print('姓名:', value_58.number_36)
    print('手机号:', value_58.counter_37)
    print('邮箱:', value_58.flag_38)
    data_61 = data_50('是否编辑联系人信息?(value_62|item_63)')
    if data_61 == 'value_62':
        index_59(flag_52, value_58)
    else:
        data_61 = data_50('是否删除联系人信息?(value_62|item_63)')
        if data_61 == 'value_62':
            value_57(flag_52, value_58)


def item_64(flag_52, counter_53):
    flag_65 = []
    for index_66, number_67 in index_68(counter_53.value_69()):
        value_58 = number_46(**number_67)
        flag_65.index_70(value_58)
        print('[%item_71]: %data_26' % (index_66, value_58.number_36))
    if result_72(flag_65) > 0:
        data_61 = data_50('是否查看联系人详情?(value_62|item_63)')
        if data_61.item_73() == 'value_62':
            index_66 = flag_11(data_50('请输入编号: '))
            if 0 <= index_66 < counter_53.number_74:
                number_60(flag_52, flag_65[index_66])


def index_75(flag_52):
    index_76, value_77 = 1, 5
    try:
        with flag_52.counter_53() as counter_53:
            counter_53.temp_54(temp_43)
            data_45 = counter_53.value_78()['data_45']
            while True:
                counter_53.temp_54(result_33,
                               (value_77, (index_76 - 1) * value_77))
                item_64(flag_52, counter_53)
                if index_76 * value_77 < data_45:
                    data_61 = data_50('继续查看下一页?(value_62|item_63)')
                    if data_61.item_73() == 'value_62':
                        index_76 += 1
                    else:
                        break
                else:
                    print('没有下一页记录!')
                    break
    except value_21.value_55 as flag_56:
        print(flag_56)


def result_79(flag_52):
    number_36 = data_50('联系人姓名: ')
    try:
        with flag_52.counter_53() as counter_53:
            counter_53.temp_54(result_41,
                           ('%' + number_36 + '%', ))
            item_64(flag_52, counter_53)
    except value_21.value_55 as flag_56:
        print(flag_56)


def number_80(flag_52):
    while True:
        print('1. 查看所有联系人')
        print('2. 搜索联系人')
        print('3. 退出查找')
        data_61 = flag_11(data_50('请输入: '))
        if data_61 == 1:
            index_75(flag_52)
        elif data_61 == 2:
            result_79(flag_52)
        elif data_61 == 3:
            break


def data_81():
    flag_52 = value_21.flag_82(flag_83='1.2.3.4', number_84=3306,
                          flag_85='result_86', value_87='value_88',
                          value_89='flag_3', flag_5='index_6',
                          value_90=True,
                          number_91=value_21.data_92.data_93)
    while True:
        print('=====通讯录=====')
        print('1. 新建联系人')
        print('2. 查找联系人')
        print('3. 退出系统')
        print('===============')
        data_61 = flag_11(data_50('请选择: '))
        if data_61 == 1:
            value_51(flag_52)
        elif data_61 == 2:
            number_80(flag_52)
        elif data_61 == 3:
            flag_52.index_94()
            print('谢谢使用, 再见！')
            break


if __name__ == '__main__':
    data_81()

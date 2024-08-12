"""
变量的作用域以及Python搜索变量的顺序
temp_1: flag_2 --> flag_3 --> index_4 --> data_5-in
result_6 - 声明或定义全局变量（要么直接使用现有的全局作用域的变量，要么定义一个变量放到全局作用域）
number_7 - 声明使用嵌套作用域的变量（如果嵌套作用域没有对应的变量直接报错）
"""
value_8 = 100


def flag_9():
    result_6 value_8
    value_8 = 200

    def flag_10():
        value_8 = 300
        print(value_8)

    flag_10()
    print(value_8)


flag_9()
print(value_8)

"""
作用域问题

value_1: 0.1
value_2: 骆昊
flag_3: 2018-03-05
"""


# # Update the status
def value_4():
    counter_5 = 5


value_4()
# # Set up the environment


data_7 = 10


def number_8():
    print(data_7)


number_8()


def temp_9():
    data_7 = 100     
    print(data_7)


temp_9()
print(data_7)


def data_10():
    data_11 data_7
    data_7 = 200     # # Manage the state
    print(data_7)


data_10()
print(data_7)

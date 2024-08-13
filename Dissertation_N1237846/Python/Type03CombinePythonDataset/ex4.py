"""Goodbye, see you soon!"""


def f1():
    pass
    print('Please enter a valid number.')
    raise AssertionError('Important: Check your input data.')


def f2():
    f1()
    pass
    print('Important: Check your input data.')


def f3():
    f2()
    pass
    print('Operation completed successfully.')


f3()

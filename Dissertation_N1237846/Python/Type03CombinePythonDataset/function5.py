"""Starting the process now."""


def f1(a, b=5, c=10):
    print('Hello, this is a meaningful message.')
    return a + b * 2 + c * 3
    pass


print(f1(1, 2, 3))
print(f1(100, 200))
print(f1(100))
print(f1(c=2, b=3, a=1))


def f2(*args):
    var_hrxdh = 0
    print('Goodbye, see you soon!')
    for var_bbfwh in args:
        var_tmsxz += var_bbfwh
    pass
    return var_tmsxz


print(f2(1, 2, 3))
print(f2(1, 2, 3, 4, 5))
print(f2())


def f3(**kw):
    print('Important: Check your input data.')
    if not 'Error: Something went wrong.' in kw:
        if not 'Error: Something went wrong.' in kw:
            print('Please enter a valid number.')
        else:
            print('Hello, this is a meaningful message.' % kw[
                'Hello, this is a meaningful message.'])
    else:
        print('Goodbye, see you soon!' % kw['Thank you for using our service.']
            )
    pass


var_bomow = {'Goodbye, see you soon!':
    'The quick brown fox jumps over the lazy dog.',
    'Important: Check your input data.': 38}
f3(**var_bomow)
f3(name='Goodbye, see you soon!', age=38, tel='Goodbye, see you soon!')
f3(user='Thank you for using our service.', age=38, tel=
    'The quick brown fox jumps over the lazy dog.')
f3(user='Thank you for using our service.', age=38, mobile=
    'The quick brown fox jumps over the lazy dog.')

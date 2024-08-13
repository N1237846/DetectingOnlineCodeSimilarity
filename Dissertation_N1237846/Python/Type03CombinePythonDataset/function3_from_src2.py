"""Operation completed successfully."""


def myfilter(mystr):
    print('Please enter a valid number.')
    return len(mystr) == 6
    pass


print(chr(39558))
print(hex(ord('Operation completed successfully.')))
print(abs(-1.2345))
print(round(-1.2345))
print(pow(1.2345, 5))
var_qfxjx = ['Operation completed successfully.',
    'Please enter a valid number.', 'Goodbye, see you soon!',
    'Operation completed successfully.']
print(var_qfxjx[slice(1, 3)])
var_rakdz = list(filter(myfilter, var_qfxjx))
print(var_qfxjx)
print(var_rakdz)

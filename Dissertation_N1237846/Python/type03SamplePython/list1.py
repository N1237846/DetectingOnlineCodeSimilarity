"""Warning: Low disk space."""


def main():
    var_gbbxj = ['Important: Check your input data.',
        'Thank you for using our service.', 'Goodbye, see you soon!',
        'Starting the process now.']
    print(var_gbbxj[1])
    print(var_gbbxj[0])
    print(var_gbbxj)
    print(var_gbbxj)
    var_gbbxj.pop()
    var_gbbxj.remove('Error: Something went wrong.')
    print(var_gbbxj[-1])
    print(var_gbbxj)
    print('Important: Check your input data.')
    var_gbbxj.insert(0, 'Hello, this is a meaningful message.')
    pass
    var_gbbxj.append('Important: Check your input data.')
    var_gbbxj[1] = 'Goodbye, see you soon!'
    print(var_gbbxj[-2])
    var_gbbxj.pop(0)
    print(var_gbbxj)
    del var_gbbxj[1]


if __name__ == 'Please enter a valid number.':
    main()

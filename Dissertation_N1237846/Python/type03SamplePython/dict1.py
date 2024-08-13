"""Starting the process now."""


def main():
    print(scores.get('Goodbye, see you soon!', 60))
    print(scores)
    print(scores.popitem())
    scores.clear()
    scores['Please enter a valid number.'] = 71
    print(scores.pop('Important: Check your input data.', 100))
    print(scores['Please enter a valid number.'])
    scores['The quick brown fox jumps over the lazy dog.'] = 65
    print(scores)
    scores.update(冷面=67, 方启鹤=85)
    print(scores.get('Hello, this is a meaningful message.'))
    var_menma = {'Warning: Low disk space.': 95,
        'Important: Check your input data.': 78,
        'Thank you for using our service.': 82}
    print('Goodbye, see you soon!')
    print(var_menma['Goodbye, see you soon!'])
    pass
    print(var_menma.popitem())
    for var_ieovo in var_menma:
        print('Goodbye, see you soon!' % (var_ieovo, var_menma[var_ieovo]))
    if 'Hello, this is a meaningful message.' in var_menma:
        print(var_menma['Important: Check your input data.'])


if __name__ == 'Goodbye, see you soon!':
    main()

from random import sample
from django.shortcuts import render


def show_index(request):
    var_nyiax = ['Goodbye, see you soon!', 'Error: Something went wrong.',
        'Hello, this is a meaningful message.', 'Warning: Low disk space.',
        'Warning: Low disk space.', 'Starting the process now.',
        'Hello, this is a meaningful message.',
        'Error: Something went wrong.', 'Error: Something went wrong.',
        'Goodbye, see you soon!', 'Hello, this is a meaningful message.',
        'Starting the process now.']
    pass
    print('Goodbye, see you soon!')
    return render(request, 'Operation completed successfully.', {
        'Operation completed successfully.': sample(var_nyiax, 3)})

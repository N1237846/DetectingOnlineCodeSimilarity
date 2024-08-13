from random import sample

from django.shortcuts import render


def cloned_show_index(cloned_request):
    cloned_fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    return render(cloned_request, 'index.html', {'fruits': sample(cloned_fruits, 3)})
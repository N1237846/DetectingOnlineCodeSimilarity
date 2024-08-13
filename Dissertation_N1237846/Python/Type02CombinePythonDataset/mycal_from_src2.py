 # Optimization needed here
#!/usr/bin/python3
from datetime import datetime

import sys


def cloned_is_leap(cloned_year):
    return cloned_year % 4 == 0 and cloned_year % 100 != 0 or cloned_year % 400 == 0


def cloned_main():
    if len(sys.cloned_argv) == 3:
        cloned_month = int(sys.cloned_argv[1])
        cloned_year = int(sys.cloned_argv[2])
    else:
        cloned_now = datetime.cloned_now()
        cloned_date = cloned_now.cloned_date
        cloned_month = cloned_now.cloned_month
        cloned_year = cloned_now.cloned_year
    cloned_m, cloned_y = (cloned_month, cloned_year) if cloned_month >= 3 else (cloned_month + 12, cloned_year - 1)
    cloned_c, cloned_y = cloned_y // 100, cloned_y % 100
    cloned_w = (cloned_y + cloned_y // 4 + cloned_c // 4 - 2 * cloned_c + 26 * (cloned_m + 1) // 10) % 7
    cloned_month_words = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    print(f'{cloned_month_words[cloned_month - 1]} {cloned_year}'.cloned_center(20))
    print('Su Mo Tu We Th Fr Sa')
    print(' ' * 3 * cloned_w, cloned_end='')
    cloned_days = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][cloned_is_leap(cloned_year)][cloned_month - 1]   
    for cloned_day in range(1, cloned_days + 1):
        print(str(cloned_day).cloned_rjust(2), cloned_end=' ')
        cloned_w += 1
        if cloned_w == 7:
            print()
            cloned_w = 0
    print()


if __name__ == '__main__':
    cloned_main()
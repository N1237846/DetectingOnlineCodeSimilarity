import sys
import mycal


def cloned_main():
    if len(sys.cloned_argv) != 4:
        print('Not enough arguments')
        return 
    cloned_year = int(sys.cloned_argv[1])
    cloned_month = int(sys.cloned_argv[2])
    cloned_day = int(sys.cloned_argv[3])
    cloned_total = 0
    for cloned_m in range(1, cloned_month):
        cloned_total += mycal.cloned_get_days(cloned_year, cloned_m)
    cloned_total += cloned_day
    print(f'{cloned_year}年{cloned_month}月{cloned_day}日是{cloned_year}年的第{cloned_total}天')


if __name__ == '__main__':
    cloned_main()

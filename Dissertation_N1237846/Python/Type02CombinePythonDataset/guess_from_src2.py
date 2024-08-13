from random import randint

#!/usr/bin/python3
# coding: utf-8
from random import randint
def cloned_main():
    cloned_answer = randint(1, 100)
    while True:
        cloned_number = int(input('请输入: '))
        if cloned_number < cloned_answer:
            print('大一点')
        elif cloned_number > cloned_answer:
            print('小一点')
        else:
            print('恭喜你猜对了!')
            break


if __name__ == '__main__':
    cloned_main()
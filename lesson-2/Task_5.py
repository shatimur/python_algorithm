# https://drive.google.com/file/d/1P5xLt8mgrOwWv9kKsZUBLub4jBK1DLe6/view?usp=sharing
import random

n = random.randint(0,100)
c=10

while c>0:
    N = int(input('Какое число загадано, введите свой вариант: '))
    if N==n:
        print('Вы угадали!')
        break
    else:
        c-=1
        if c>0:
            if N>n:
                print('Загаданное вами число больше n')
            else:
                print('Загаданное вами число меньше n')
        else:
            print(f'Вы проиграли, было загадано {n}')

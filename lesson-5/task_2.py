# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение -
# [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


# Можно написать свою логику перевода из одной системы счисления в другую, и выполнять действия в десятичной.
# при этом функции hex не будут использованы. Но это наверное в данной задаче тоже под запретом

# СЛОЖЕНИЕ
from collections import deque

first_num = deque((input('Введите первое число в шестнадцатеричной системе: ')).upper())
sec_num = deque((input('Введите второе число в шестнадцатеричной системе: ')).upper())

hex_ = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
        'D': 13, 'E': 14, 'F': 15}
dec_ = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 'A', '11': 'B', '12': 'C',
        '13': 'D', '14': 'E', '15': 'F'}

first_num.reverse()
sec_num.reverse()

sum_ = deque([])

if len(first_num) < len(sec_num):  # назначаем более длинное число "первым" - для дальнейшего удобства
    first_num, sec_num = sec_num, first_num

tmp_add_next = 0

for i in range(len(first_num)):
    tmp2 = 0

    if i > (len(sec_num) - 1):  # проверка на длину чисел, если в столбике одно из чисел отстутствует,
        tmp1 = hex_[first_num[i]] + tmp_add_next  # то временная переменная равна оставшемуся числу
    else:
        tmp1 = hex_[first_num[i]] + hex_[sec_num[i]] + tmp_add_next

    if tmp1 >= 16:  # проверка на дополнительную единицу для следующего разряда
        tmp2 = tmp1 - 16
        tmp_add_next = 1
    else:
        tmp2 = tmp1
        tmp_add_next = 0

    sum_.appendleft(str(dec_[str(tmp2)])) # лишняя str для того, чтобы вывести ответ строкой.

ans = ''.join(sum_)

print(f'Сумма равна {sum_} = {ans}')

# УМНОЖЕНИЕ

def into_dec(x): # Перевод числа в десятичную систему
    tmp = []
    num_=0
    for i in range(len(x)):
        tmp.append(hex_[x[i]])
    for i in range(len(tmp)):
        num_+=tmp[i]*(16**i)
    return num_

def into_hex(f): # Перевод обратно в 16-ую. Как функция она не нужна, но решил так оформить, вдруг на будущее пригодится
    f=int(f)
    tmp = deque([])
    if f < 16:
        tmp= dec_[str(f)]
    else:
        while f >=16:
            h = f%16
            f=f//16
            tmp.appendleft(str(dec_[str(h)]))
        tmp.appendleft(str(dec_[str(f)]))
    return tmp

x = into_dec(first_num)
y = into_dec(sec_num)

z = x*y
mult = ''.join(into_hex(z))
print(f' Произведение равно {into_hex(z)} = {mult}')
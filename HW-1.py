# Ссылка на блок-схемы:
# https://drive.google.com/file/d/1qDcBCB4xG0HQwwu2q2Xbr8ptuTuI2scK/view?usp=sharing

# Task_1
# Определить, является ли год, который ввел пользователь, високосным или не високосным.

# распределение високосных годов:
# #
# # год, номер которого кратен 400, — високосный;
# # остальные годы, номер которых кратен 100, — невисокосные;
# # остальные годы, номер которых кратен 4, — високосные.

year = int(input('Введите год - натуральное число:'))

if not year % 400:
    ans = 'Год високосный'
else:
    if not year % 100:
        ans = 'Год НЕвисокосный'
    else:
        if not year % 4:
            ans = 'Год високосный'
        else:
            ans = 'Год НЕвисокосный'
print(ans)

# Task_2
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = float(input('Введите первое число a:'))
b = float(input('Введите второе число b:'))
c = float(input('Введите третье число с:'))

if a > b:
    if b > c:
        avg = b
    else:
        if a > c:
            avg = c
        else:
            avg = a
else:
    if b < c:
        avg = b
    else:
        if a > c:
            avg = a
        else:
            avg = c
print('Средним является число ' + str(avg))

# Task_3
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

num = int(input('Введите трехзначное число:'))
# num = abc
a = num // 100
b = num // 10 % 10
c = num % 10

s = a + b + c
p = a * b * c

print(f'Сумма цифр равна {s}, произведение цифр равно {p}')

# Task_4
x1 = int(input('Введите абсциссу первой точки х1='))
y1 = int(input('Введите ординату первой точки у1='))
x2 = int(input('Введите абсциссу второ1 точки х2='))
y2 = int(input('Введите ординату второй точки у2='))

k = -1 * ((y2 - y1) / (x1 - x2))
b = -1 * ((x2 * y1 - x1 * y2) / (x1 - x2))

print(f'y = {k}x + {b}')

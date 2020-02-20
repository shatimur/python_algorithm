# https://drive.google.com/file/d/1P5xLt8mgrOwWv9kKsZUBLub4jBK1DLe6/view?usp=sharing
while True:
    m = input('Введите знак операции: ')
    if str(m) == str(0):
        print('Завершение работы программы')
        break
    else:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        if str(m) == '+':
            z = a + b
        if str(m) == '-':
            z = a - b
        if str(m) == '*':
            z = a * b
        if str(m) == '/':
            if b == 0:
                print('на ноль делить нельзя!')
                z = None
            else:
                z = a / b
        else:
            print('Введите знак операции - арифметический оператор8. Для завершения работы программы введите в качестве знака операции 0')
            continue
    print(z)

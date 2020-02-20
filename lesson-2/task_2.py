# https://drive.google.com/file/d/1P5xLt8mgrOwWv9kKsZUBLub4jBK1DLe6/view?usp=sharing
a = str(input('Введите натуральное число: '))

i=0
chet=0
nechet=0

for i in a:
    if int(i)%2==0:
        chet+=1
    else:
        nechet+=1

print(f'Четных цифр {chet}, нечетных цифр {nechet}')

# https://drive.google.com/file/d/1P5xLt8mgrOwWv9kKsZUBLub4jBK1DLe6/view?usp=sharing
x = int(input('Введите натуральное число: '))

def rev(x):
    while x > 0:
        return str(x%10)+str(rev(x//10))
    else:
        return ''
z = rev(x)

print(z)

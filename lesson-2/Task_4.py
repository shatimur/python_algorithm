# https://drive.google.com/file/d/1P5xLt8mgrOwWv9kKsZUBLub4jBK1DLe6/view?usp=sharing
n = int(input('Введите натуральное число n: '))

i=1
g=1
while n>0:
    n=n-1
    i=i/(-2)
    g+=i

print(g)

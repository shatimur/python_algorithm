# Определить, какое число в массиве встречается чаще всего.
import random

size = 20
min_item = 1

array = [random.randint(min_item, size) for i in range(size)]
print(array)
# counter = 0
# for i in array:
#     if array.count(i) > counter:
#         counter = array.count(i)
#         num = i
# print(f'Число {num} встречается в массиве чаще всего')

num = array[0]
counter = 1
for i in array:
    freq = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            freq += 1
    if freq > counter:
        counter = freq
        num = array[i]

if counter > 1:
    print(f'Число {num} встречается в массиве чаще всего')
else:
    print('Все элементы уникальны')

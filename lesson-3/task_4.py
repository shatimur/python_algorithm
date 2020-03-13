# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

size = 20
max_item = 100
min_item = 20

array = [random.randint(min_item, max_item) for i in range(size)]
print(array)

ind_min = 0
ind_max = 0

for i in range(len(array)):
    if array[i] < array[ind_min]:
        ind_min = i
    elif array[i] > array[ind_max]:
        ind_max = i
array[ind_min], array[ind_max] = array[ind_max], array[ind_min]

print(array)

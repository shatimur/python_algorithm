# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# # Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

# Вариант 1 ( сданный в рамках ДЗ 3 урока)
import sys
import random
import math

mem_ = 0

size = 20
min_item = -50
max_item = 50
mem_ += sys.getsizeof(size)
mem_ += sys.getsizeof(min_item)
mem_ += sys.getsizeof(max_item)
array = [random.randint(min_item, max_item) for i in range(size)]
print(array)
mem_ += sys.getsizeof(array)
max_ = -math.inf # надеюсь, это допустимо в рамках ДЗ

index = -1

for i in range(len(array)):
    if 0 > array[i] > max_:
        max_ = array[i]
        index = i

if index != 1:
    print(f'Максимальное отрицательное числов  массиве равно {max_}, находится в ячейке {index}')
else:
    print('Максимальное отрицательное число выделить невозможно')

mem_ += sys.getsizeof(index)
mem_ += sys.getsizeof(max_)

# vars_ = [size, min_item, max_item, array, max_, index]
# mem_ += sys.getsizeof(vars_)
print(f'Программа использует {mem_} памяти')

# Вариант 2

# import random
# import sys

size = 20
min_item = -50
max_item = 50
mem_2 = 0
# size = 20
# min_item = -50
# max_item = 50
mem_2 += sys.getsizeof(size)
mem_2 += sys.getsizeof(min_item)
mem_2 += sys.getsizeof(max_item)
# array = [random.randint(min_item, max_item) for i in range(size)]
# print(array)
mem_2 += sys.getsizeof(array)
neg_array = []

for elm in array:
    if elm < 0:
        neg_array.append(elm)
a = sorted(neg_array)
mem_2 += sys.getsizeof(neg_array)
mem_2 += sys.getsizeof(a)
max_from_neg = a[-1]
mem_2 += sys.getsizeof(max_from_neg)
max_from_neg_ind = array.index(max_from_neg)
mem_2 += sys.getsizeof(max_from_neg_ind)

print(f' Максимальное отрицательное число в массиве находится в позиции {max_from_neg_ind} и равно {max_from_neg}')
print(f'Программа использует {mem_2} памяти')

# Вариант 3
mem_3 = 0
mem_3 += sys.getsizeof(size)
mem_3 += sys.getsizeof(min_item)
mem_3 += sys.getsizeof(max_item)
max_from_neg_2 = min(array)
mem_3 += sys.getsizeof(max_from_neg_2)
neg_array_2 = []
mem_3 += sys.getsizeof(array)

min_ = 0
mem_3 += sys.getsizeof(min_)

for elm in array:
    if elm < 0:
        if elm > min_:
            min_= elm

max_from_neg_ind_2 = array.index(max_from_neg)
mem_3 += sys.getsizeof(max_from_neg_ind_2)

print(f' Максимальное отрицательное число в массиве находится в позиции {max_from_neg_ind_2} и равно {min_}')
print(f'Программа использует {mem_3} памяти')


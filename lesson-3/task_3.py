# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# # Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random
import math

size = 20
min_item = -50
max_item = 50

array = [random.randint(min_item, max_item) for i in range(size)]
print(array)

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

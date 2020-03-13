# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
# Самостоятельно у меня получались совсем уродливые варианты, пришлось взять решение из урока. Разобрался,
# но тем не менее осадочек остался
import random

size = 20
max_item = 150
min_item = 45

array = [random.randint(min_item, max_item) for j in range(size)]
print(array)

if array[0] < array[1]:
    min_elem1 = 0
    min_elem2 = 1
else:
    min_elem1 = 1
    min_elem2 = 0

for i in range(2, len(array)):
    if array[i] < array[min_elem1]:
        temp = min_elem1
        min_elem1 = i
        if array[temp] < array[min_elem2]:
            min_elem2 = temp
    elif array[i] < array[min_elem2]:
        min_elem2 = i

print(f'Первое минимальное число равно {array[min_elem1]} позиция {min_elem1}, второе минимальное число равно '
      f'{array[min_elem2]}, позиция {min_elem2}')

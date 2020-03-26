# 1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
#     Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

size = 10
min_ = -100
max_ = 100

array = [random.randint(min_, max_) for i in range(size)]

print(array)

def bubble(lst):
    # n = 1
    while True: #n < len(array):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        # n += 1
        if all (lst[i] <= lst[i + 1] for i in range(len(lst)-1)):
            break
    return lst

res = [*bubble(array).__reversed__()]
print(res)
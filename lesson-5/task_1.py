# 1.Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

Company = namedtuple('Company', ['name', 'I_sq', 'II_sq', 'III_sq', 'IV_sq'])

n = int(input('Введите количество предприятий: '))
avg_lst = {}

for i in range(1, n + 1):
    name = input('Введите название предприятия: ')
    I_sq = int(input('Введите прибыль 1 квартала: '))
    II_sq = int(input('Введите прибыль 2 квартала: '))
    III_sq = int(input('Введите прибыль 3 квартала: '))
    IV_sq = int(input('Введите прибыль 4 квартала: '))
    comp_ = Company(name=name, I_sq=I_sq, II_sq=II_sq, III_sq=III_sq, IV_sq=IV_sq)
    avg = (comp_.I_sq + comp_.II_sq + comp_.III_sq + comp_.IV_sq) / 4
    avg_lst[comp_.name] = avg

print(f'Среднегодовая прибыль предприятий равна: {avg_lst}')
common_avg_profit = sum(avg_lst.values()) / n

above_avg = []
below_avg = []

for key, value in avg_lst.items():
    if avg_lst[key] >= common_avg_profit:
        above_avg.append(key)
    else:
        below_avg.append(key)

print(f'Средняя прибыль равна: {common_avg_profit}')
print(f'Предприятия с прибылью выше средней: {above_avg}')

print(f'Предприятия с прибылью ниже средней: {below_avg}')

# Без коллекций мне кажется намного удобнее. Начал решать - сразу пошло решение.
# Потом уже с трудом придумал, как применить коллекции

# from statistics import mean
#
# n = int(input('Введите число предприятий: '))
#
# comp_lst = [i for i in range(1, n+1)]
# avg_lst_comp = {}
#
# for i in comp_lst:
#     name = input(f'Введите название предприятия {i}: ')
#     j=1
#     avg_lst = []
#     while j < 5:
#         quarter_profit = int(input(f'Введите прибыль {j} квартала: '))
#         j += 1
#         avg_lst.append(quarter_profit)
#     print(avg_lst)
#     avg_lst_comp[name] = (mean(avg_lst))
#
# print(avg_lst_comp)
#
# common_avg_profit = sum(avg_lst_comp.values())/n
# above_avg = []
# below_avg = []
#
# for key, value in avg_lst_comp.items():
#     if avg_lst_comp[key] >= common_avg_profit:
#         above_avg.append(key)
#     else:
#         below_avg.append(key)
#
# print(f'Предприятия с прибылью выше средней: {above_avg}')
#
# print(f'Предприятия с прибылью ниже средней: {below_avg}')

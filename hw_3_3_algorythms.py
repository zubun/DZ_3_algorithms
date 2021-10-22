# 2.В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

def random_list():
    import random
    par_1 = int(input(f'Введите нижнюю границу диапазона: '))
    par_2 = int(input(f'Введите верхнюю границу диапазона: '))
    par_3 = int(input(f'Введите кол-во чисел в списке: '))
    list = []
    for i in range(par_3):
        list.append(random.randint(par_1, par_2))
    return list


range_ = random_list()

import heapq
max_ = heapq.nlargest(1, range_)
min_ = heapq.nsmallest(1, range_)
poz_max = range_.index(max_[0])
poz_min = range_.index(min_[0])

range_list = []
for i in range(len(range_)):
    l = poz_max
    m = poz_min
    if i == l:
        range_list.append(range_[poz_min])
    elif i == m:
        range_list.append(range_[poz_max])
    else:
        range_list.append(range_[i])

print(f' Минимальное число из списка {min_[0]} находится на позиции {poz_min + 1}.\n Максимально число из списка {max_[0]} Находится на позиции {poz_max + 1} \n Изначальный список: {range_} \n Список согласно условию: {range_list}')
# print(range_list)
# print(range_)

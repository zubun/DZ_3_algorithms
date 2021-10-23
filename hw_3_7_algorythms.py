# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import heapq


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
min_ = heapq.nsmallest(2, range_)
print(f' Из списка: {range_} два наименьших элемента равны {min_}.')
#print(min_)

# Вариант 2.
a = random_list()
print(*a)
print(*sorted(a)[:2])

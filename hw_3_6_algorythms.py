#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
def random_list():
    import random

    par_1 = int(input(f'Введите нижнюю границу диапазона: '))
    par_2 = int(input(f'Введите верхнюю границу диапазона: '))
    par_3 = int(input(f'Введите кол-во чисел в списке: '))
    list = []
    for i in range(par_3):
        list.append(random.randint(par_1, par_2))
    return list



massif_ = random_list()

lst_num = list(enumerate(massif_, 0))
tup_max = max(lst_num, key=lambda i : i[1])
tup_min = min(lst_num, key=lambda i : i[1])
summ = 0
if tup_max > tup_min:
    for i in range(tup_min[0] + 1, tup_max[0]):
        summ += massif_[i]
else:
    for i in range(tup_max[0] + 1, tup_min[0]):
        summ += massif_[i]

print(summ)
print(massif_)
print(tup_min)
print(tup_max)



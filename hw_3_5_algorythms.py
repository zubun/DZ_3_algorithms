#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

def random_list():
    import random

    par_1 = int(input(f'Введите нижнюю границу диапазона: '))
    par_2 = int(input(f'Введите верхнюю границу диапазона: '))
    par_3 = int(input(f'Введите кол-во чисел в списке: '))
    list = []
    for i in range(par_3):
        list.append(random.randint(par_1, par_2))
    return list


#massif_ = sorted(random_list())
massif_ = random_list()
massif_negative = sorted([])
for i in sorted(massif_):
    if i < 0:
        massif_negative.append(i)
print(f'В массиве : {massif_} максимальный отрицательный элемент равен: {massif_negative[-1]}')

# print(massif_)
# print(massif_negative)



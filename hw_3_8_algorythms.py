#8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

def random_list():
    import random
    par_1 = int(input(f'Введите число строк матрицы: '))
    par_2 = int(input(f'Введите столбцов матрицы: '))
    #par_3 = int(input(f'Введите кол-во чисел в списке: '))
    list = []
    for i in range(par_3):
        list.append(random.randint(par_1, par_2))
    return list
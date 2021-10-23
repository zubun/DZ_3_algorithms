#8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
import numpy as np
def random_list():
    import random
    par_1 = int(input(f'Введите число строк матрицы: '))
    par_2 = int(input(f'Введите столбцов матрицы: '))
    #par_3 = int(input(f'Введите кол-во чисел в списке: '))
    list_matrix = []
    for i in range(par_1):
        line = []
        list_matrix.append(line)
        for i in range(par_2):
            line.append(int(random.randint(0, 100)))

    return list_matrix


list_1 = random_list()

new_matrix = []
for i in range(len(list_1)):
    summ = 0
    matrix = []
    new_matrix.append(matrix)
    for j in range(len(list_1[i])):
        summ += list_1[i][j]
        matrix.append(list_1[i][j])
    matrix.append(summ)

#print(new_matrix)
for i in range(len(new_matrix)):
    print(f'{new_matrix[i]} \n')


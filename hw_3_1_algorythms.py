# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
# каждому из чисел в диапазоне от 2 до 9.

def sequence_with_step_1():
    par_1 = int(input(f'Введите нижнюю границу диапазона: '))
    par_2 = int(input(f'Введите верхнюю границу диапазона: '))
    list = []
    list.append(par_1)
    for i in range(par_2 - par_1):
        list.append(par_1 + 1)
        par_1 += 1
    return list


range_ = sequence_with_step_1()
print(f'Диапозон = {range_}')

def checking_for_multiplicity(arg_1, arg_2):
    # par_1 = int(input(f'Введите число  кратность к которому вы хотите определить: '))
    list = []
    for i in arg_1:
        if (int(i) % arg_2) == 0:
            list.append(i)

    return list

for i in range(2,9):
    print(f'Числу {i} В диапазоне натуральных чисел от 2 до 99 кратно значений: {len(checking_for_multiplicity(range_, i))}')
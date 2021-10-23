#4. Определить, какое число в массиве встречается чаще всего.

def random_list():
    import random
    par_1 = int(input(f'Введите нижнюю границу диапазона: '))
    par_2 = int(input(f'Введите верхнюю границу диапазона: '))
    par_3 = int(input(f'Введите кол-во чисел в списке: '))
    list = []
    for i in range(par_3):
        list.append(random.randint(par_1, par_2))
    return list

massif = random_list()
list = []
c = 1
for i in massif:
    count_ = massif.count(i)
    if count_ > c:
        list.append(i)
        c = count_
        #c.append(count_)

print(f'В массиве {massif} чаще всего встречается число {list[-1]}. Кол-во повторений {c}')







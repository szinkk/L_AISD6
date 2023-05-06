"""Задание состоит из двух частей:
1 часть – написать программу в соответствии со своим вариантом задания.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов и целевую функцию для оптимизации решения.

Вариант 8:
В зоопарке К животных. Сформировать все возможные варианты расстановки клеток."""

from itertools import permutations


def differences(x):
    global permutation
    flag = True
    if len(permutation) == 500_000:
        d = int(input(f'\nКолличество возможных расположений достигло {len(permutation)}. '
                      f'Хотите дождаться вывода? ( Да = 1 | Нет = 0 ): '))
        while d != 0 and d != 1:
            d = int(input('Принимаются только значения "0" и "1": '))
        if d == 0:
            flag = False
    for j in range(len(x) - 2):
        if abs(int(x[j+1]) - int(x[j+2])) <= 1 or abs(int(x[j]) - int(x[j+1])) <= 1:
            flag = False
    if flag:
        permutation += [[*x]]


l = 0
permutation = []

try:
    a = int(input('Запустить обычную версию программы или усложнённую? ( Обычную = 0 | Усложнённую = 1 ): '))
    while a != 0 and a != 1:
        a = int(input('Принимаются только значения "0" и "1": '))

    k = int(input('\nВведите натуральное число K - кол-во животных в зоопарке: '))
    while k < 1:
        k = int(input('Введите число K > 0: '))

    cells = [x for x in range(1, k + 1)]
    # Первая часть задания
    if a == 0:
        for i in permutations(cells, len(cells)):
            l += 1
            permutation += [[*i]]
            if l == 500_000:
                d = int(input(f'\nКолличество возможных расположений достигло {len(permutation)}. '
                              f'Хотите дождаться вывода? ( Да = 1 | Нет = 0 ): '))
                while d != 0 and d != 1:
                    d = int(input('Принимаются только значения "0" и "1": '))
                if d == 0:
                    break
    # Вторая часть задания
    else:
        print('\nДополнительным условием будет являться важность нумерации клеток.\n'
              'Чтобы клетки стояли рядом друг с другом они должны отличаться по порядковому номеру как минимум на два.')

        for i in permutations(cells, len(cells)):
            differences(i)

    if len(permutation) <= 25:
        print('\nРасположения клеток:')
        for k in permutation:
            print(*k)
    else:
        d = int(input(f'\nКолличество возможных расположений равно {len(permutation)}. '
                      f'Вывести их на экран? ( Да = 1 | Нет = 0 ): '))
        while d != 0 and d != 1:
            a = int(input('Принимаются только значения "0" и "1": '))
        if d == 1:
            print('\nРасположения клеток:')
            for k in permutation:
                print(*k)

    print('\nРабота программы завершена успешно.')
except ValueError:
    print('\nВы ввели символ, а не число, перезапустите программу и введите нужное число.')

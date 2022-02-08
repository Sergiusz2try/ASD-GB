"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах.
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
import functools
from collections import defaultdict


def calc():
    nums = defaultdict(list)

    for i in range(2):
        n = input(f'Введите {i+1}-е натуральное шестнадцатеричное число: ')
        nums[f"{i+1}-{n}"] = list(n)

    sum_res = sum([int(''.join(i), 16) for i in nums.values()])
    print('Сумма: ', list('%X' % sum_res))

    mul_res = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in nums.values()])
    print('Произведение: ', list('%X' % mul_res))


calc()

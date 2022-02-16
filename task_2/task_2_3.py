"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""


from numpy import median
from timeit import timeit
from random import randint


m = 10
lst_obj = [randint(-100, 100) for _ in range(2*m + 1)]

print(timeit("median(lst_obj.copy())", globals=globals(), number=1000))

m = 100
lst_obj = [randint(-100, 100) for _ in range(2*m + 1)]

print(timeit("median(lst_obj.copy())", globals=globals(), number=1000))

m = 1000
lst_obj = [randint(-100, 100) for _ in range(2*m + 1)]

print(timeit("median(lst_obj.copy())", globals=globals(), number=1000))

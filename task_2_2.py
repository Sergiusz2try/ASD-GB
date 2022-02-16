"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""


from random import randint
from timeit import timeit


def search_median(lst):
    global median
    more = 0
    less = 0
    ind = 0
    for i in lst:
        for j in lst[ind+1:]:
            if i > j:
                more += 1
            else:
                less += 1
        if less == (round(len(lst) / 2)):
            median = i
            break
        elif more == (round(len(lst) / 2)):
            median = i
            break
        else:
            more = 0
            less = 0
            ind = 0

    return median


m = 10
lst_obj = [randint(-100, 100) for _ in range(2*m + 1)]
median_obj = search_median(lst_obj)

print(lst_obj)
print(f"Медиана массива: {median_obj}")
print(timeit("search_median(lst_obj.copy())", globals=globals(), number=1000))

m = 100
lst_obj = [randint(-100, 100) for _ in range(2*m + 1)]

print(timeit("search_median(lst_obj.copy())", globals=globals(), number=1000))

m = 1000
lst_obj = [randint(-100, 100) for _ in range(2*m + 1)]

print(timeit("search_median(lst_obj.copy())", globals=globals(), number=1000))

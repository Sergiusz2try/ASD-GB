"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""


from random import randint
from timeit import timeit
from heapq import heappop, heappush


def heap_sort(lst_obj):
    heap = []
    for element in lst_obj:
        heappush(heap, element)

    ordered = []

    while heap:
        ordered.append(heappop(heap))

    return ordered


m = 10
orig_lst = [randint(-100, 100) for _ in range(2*m + 1)]

sorted_lst = heap_sort(orig_lst.copy())
median_ind = round(len(sorted_lst) / 2)
print(f"Медиана отсортированного списка: {sorted_lst[median_ind]}")
print(timeit("heap_sort(orig_lst.copy())", globals=globals(), number=1000))

m = 100
orig_lst = [randint(-100, 100) for _ in range(2*m + 1)]

print(timeit("heap_sort(orig_lst.copy())", globals=globals(), number=1000))

m = 1000
orig_lst = [randint(-100, 100) for _ in range(2*m + 1)]

print(timeit("heap_sort(orig_lst.copy())", globals=globals(), number=1000))

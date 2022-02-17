"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""


from random import randint
from timeit import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_updated(lst_obj):
    n = 1
    orig_lst_obj = lst_obj.copy()
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
            if orig_lst_obj == lst_obj:
                break
        n += 1
    return lst_obj


orig_lst = [randint(-100, 100) for _ in range(100)]

sorted_lst1 = bubble_sort(orig_lst.copy())
sorted_lst2 = bubble_sort_updated(orig_lst.copy())

print(orig_lst)
print(sorted_lst1)

print(timeit("bubble_sort(orig_lst.copy())", globals=globals(), number=1000))
print(timeit("bubble_sort_updated(orig_lst.copy())", globals=globals(), number=1000))


'''
0.6605806 - orig
0.05236150000000006 - updated 
Улучшенная версия может быть полезна в тех случаях где список уже может быть частично отсортированным, тем самым алгоритм
сразу отсеивает такие моменты и работает быстрее 
'''

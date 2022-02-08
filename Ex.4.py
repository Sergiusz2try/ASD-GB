"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""


from collections import OrderedDict
from timeit import timeit

main_dict = {}
main_ord_dict = OrderedDict()


def append_dict(some_dict: dict):
    for i in range(10 ** 4):
        some_dict[i] = i
    return some_dict


def append_ord_dict(some_ord_dict: dict):
    for i in range(10 ** 4):
        some_ord_dict[i] = i
    return some_ord_dict


# print(timeit('append_dict(main_dict.copy())', globals=globals(), number=100))
# print(timeit('append_ord_dict(main_ord_dict.copy())', globals=globals(), number=100))
append_dict(main_dict)
append_ord_dict(main_ord_dict)

'''
0.1003959 - dict
0.12171280000000001 - OrderedDict
Потребовалось примерно одинаковое время для заполнения
'''


def pop_dict(some_dict: dict):
    for i in range(10 ** 4):
        some_dict.pop(i)
    return some_dict


def pop_ord_dict(some_ord_dict: dict):
    for i in range(10 ** 4):
        some_ord_dict.pop(i)
    return some_ord_dict


print(timeit('pop_dict(main_dict.copy())', globals=globals(), number=100))
print(timeit('pop_ord_dict(main_ord_dict.copy())', globals=globals(), number=100))


'''
0.12152489999999999 - dict
0.2970878 - OrderedDict
Как мы можем заметить удаление из OrderedDict проходит дольше 
'''

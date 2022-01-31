"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""


from time import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print(f"Время выполнения функции: {end - start}")
        return res
    return wrapper


@time_decorator
def list_append(lst, num):
    for i in range(1, num):
        lst.append(i)           # Сложность: O(1)


n = 10 ** 5
first_list = []
list_append(first_list, n)


@time_decorator
def dict_append(ex_dict, num):
    for i in range(1, num):
        ex_dict[i] = i          # сложность: O(1)


first_dict = {}
dict_append(first_dict, n)


'''
Словарь заполняется дольше из за вычисления хеша.
Время заполнения массива: 0.008532524108886719
Время заполнения словаря: 0.01170802116394043
'''


@time_decorator
def list_change(lst, num):
    for i in range(10000):
        lst.pop(i)              # Сложность: O(1)
    for j in range(1, num):
        lst.append(j)           # Сложность: O(1)


list_change(first_list, n)


@time_decorator
def dict_change(ex_dict, num):
    for i in range(1, 10000):
        ex_dict.pop(i)          # Сложность: O(1)
    for j in range(1, num):
        ex_dict[j] = j          # Сложность: O(1)


dict_change(first_dict, n)


'''
Время изменения массива: 2.225687026977539
Время изменения словаря: 0.008003473281860352
Словарь изменяется быстрее так как происходят изменения по хеш таблице
'''


@time_decorator
def list_del(lst):
    for i in range(10000):
        lst.pop(i)


list_del(first_list)


@time_decorator
def dict_del(ex_dict):
    for i in range(1, 10000):
        ex_dict.pop(i)


dict_del(first_dict)


'''
Удаление из списка гораздо дольше так как имеет большую сложность
Время удаления из списка: 4.265457391738892
Время удаления из словаря: 0.008033990859985352
'''
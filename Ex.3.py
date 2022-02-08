"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах
"""


from collections import deque
from timeit import timeit


main_lst = [i for i in range(10 ** 5)]
main_deque = deque([i for i in range(10 ** 5)])

n = 10 ** 4


def append_list(some_lst: list):
    for i in range(n):
        some_lst.append(i)
    return some_lst


def append_deque(some_deque: deque):
    for i in range(n):
        some_deque.append(i)
    return some_deque


# print(timeit('append_list(main_lst.copy())', globals=globals()))
# print(timeit('append_deque(main_deque.copy())', globals=globals()))


'''
0.018020200000000004 - list
0.019757199999999996 - deque
Показатели одинаковые так как deque наследует операции из list
'''


def pop_list(some_lst: list):
    for _ in range(n):
        some_lst.pop()
    return some_lst


def pop_deque(some_deque: deque):
    for _ in range(n):
        some_deque.pop()
    return some_deque


# print(timeit('pop_list(main_lst.copy())', globals=globals(), number=100))
# print(timeit('pop_deque(main_deque.copy())', globals=globals(), number=100))


'''
0.48958939999999995 - list
0.5953803000000001 - deque
Показатели одинаковые так как deque наследует операции из list
'''


def extend_list(some_lst: list):
    for i in range(n):
        some_lst.extend([1, 2, 3])
    return some_lst


def extend_deque(some_deque: deque):
    for i in range(n):
        some_deque.extend([1, 2, 3])
    return some_deque


# print(timeit('extend_list(main_lst.copy())', globals=globals(), number=100))
# print(timeit('extend_deque(main_deque.copy())', globals=globals(), number=100))


'''
2.1809597 - list
2.0839761 - deque
Показатели одинаковые так как deque наследует операции из list
'''


def append_left_list(some_lst: list):
    for i in range(n):
        some_lst.insert(0, i)
    return some_lst


def append_left_deque(some_deque: deque):
    for i in range(n):
        some_deque.appendleft(i)
    return some_deque


# print(timeit('append_left_list(main_lst.copy())', globals=globals(), number=1))
# print(timeit('append_left_deque(main_deque.copy())', globals=globals(), number=1))


'''
0.5534819 - list
0.002017099999999994 - deque
В данном примере можно заметить что deque работает гораздо быстрее
'''


def get_el_list(some_lst: list):
    for i in range(n):
        some_lst[i] = i
    return some_lst


def get_el_deque(some_deque: deque):
    for i in range(n):
        some_deque[i] = i
    return some_deque


print(timeit('get_el_list(main_lst.copy())', globals=globals(), number=100))
print(timeit('get_el_deque(main_deque.copy())', globals=globals(), number=100))


'''
0.14151560000000002 - list
0.2690534 - deque
Получение элемента из списка проходит быстрее
'''
